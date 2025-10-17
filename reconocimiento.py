import speech_recognition as sr
import os
import sounddevice as sd
import numpy as np
import wave
import tempfile

class ReconocimientoVoz:
    """Manejar el reconocimiento de voz (Speech-to-Text)"""
    
    def __init__(self):
        """Inicializa el reconocedor de voz"""
        self.recognizer = sr.Recognizer()
    
    def audio_a_texto(self, archivo_audio, idioma='es-ES'):
        """
        Convierte un archivo de audio WAV a texto
        Args:
            archivo_audio (str): Ruta del archivo WAV
            idioma (str): Código del idioma (por defecto español)
        Returns:
            str: Texto reconocido o None si hay error
        """
        if not os.path.exists(archivo_audio):
            print(f"Error: El archivo '{archivo_audio}' no existe")
            return None
        
        print(f"\n Procesando archivo: {archivo_audio}")
        
        try:
            # Cargar el archivo de audio
            with sr.AudioFile(archivo_audio) as source:
                # Ajustar para ruido ambiente
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Grabar el audio del archivo
                audio_data = self.recognizer.record(source)
                
                print("Reconociendo voz...")
                
                # Reconocer el audio usando Google Speech Recognition
                texto = self.recognizer.recognize_google(audio_data, language=idioma)
                
                print(f"Texto reconocido: '{texto}'")
                return texto
                
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
            return None
        except sr.RequestError as e:
            print(f"Error en el servicio de reconocimiento: {e}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def grabar_desde_microfono(self, duracion=5, idioma='es-ES'):
        """
        Graba audio desde el micrófono y lo convierte a texto
        Args:
            duracion (int): Duración de la grabación en segundos
            idioma (str): Código del idioma
        Returns:
            str: Texto reconocido o None si hay error
        """
        print(f"\nGrabando desde el micrófono por {duracion} segundos...")
        
        try:
            # Configuración de audio
            sample_rate = 16000  # Hz
            channels = 1  # Mono
            
            print("¡Habla ahora!")
            
            # Grabar audio usando sounddevice
            audio_data = sd.rec(int(duracion * sample_rate), 
                               samplerate=sample_rate, 
                               channels=channels, 
                               dtype='int16')
            sd.wait()  # Esperar a que termine la grabación
            
            print("Grabación completada. Procesando...")
            
            # Crear un archivo temporal WAV
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
                temp_filename = temp_file.name
                
                # Guardar el audio en formato WAV
                with wave.open(temp_filename, 'wb') as wf:
                    wf.setnchannels(channels)
                    wf.setsampwidth(2)  # 16 bits = 2 bytes
                    wf.setframerate(sample_rate)
                    wf.writeframes(audio_data.tobytes())
            
            # Usar el archivo temporal para reconocimiento
            with sr.AudioFile(temp_filename) as source:
                audio = self.recognizer.record(source)
                
                print("Reconociendo voz...")
                texto = self.recognizer.recognize_google(audio, language=idioma)
                
                print(f"✓ Texto reconocido: '{texto}'")
                
                # Eliminar archivo temporal
                os.unlink(temp_filename)
                
                return texto
                
        except sr.UnknownValueError:
            print("✗ No se pudo entender el audio")
            return None
        except sr.RequestError as e:
            print(f"✗ Error en el servicio de reconocimiento: {e}")
            return None
        except Exception as e:
            print(f"✗ Error inesperado: {e}")
            return None


def menu_reconocimiento():
    """Menú para la funcionalidad de reconocimiento de voz"""
    reconocimiento = ReconocimientoVoz()
    
    while True:
        print("\n" + "="*60)
        print("RECONOCIMIENTO DE VOZ (Speech-to-Text)")
        print("="*60)
        print("1. Convertir archivo WAV a texto")
        print("2. Grabar desde micrófono y convertir a texto")
        print("3. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            archivo = input("\nIngresa la ruta del archivo WAV: ").strip()
            if archivo:
                idioma = input("Idioma (es-ES/en-US) [es-ES]: ").strip() or "es-ES"
                reconocimiento.audio_a_texto(archivo, idioma)
            else:
                print("No se ingresó ninguna ruta")
        
        elif opcion == "2":
            try:
                duracion = int(input("Duración de grabación en segundos [max 5 seg]: ").strip() or "5")
                idioma = input("Idioma (es-ES/en-US) [es-ES]: ").strip() or "es-ES"
                reconocimiento.grabar_desde_microfono(duracion, idioma)
            except ValueError:
                print("Duración inválida, usando 5 segundos por defecto")
                reconocimiento.grabar_desde_microfono(5)
        
        elif opcion == "3":
            break
        
        else:
            print("Opción inválida")