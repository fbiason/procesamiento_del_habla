import pyttsx3

class SintesisVoz:
    """Como manejar la síntesis de voz (Text-to-Speech)"""
    
    def __init__(self):
        """Inicializa el motor de síntesis de voz"""
        self.engine = pyttsx3.init()
        self._configurar_motor()
    
    def _configurar_motor(self):
        """Configura las propiedades del motor de voz"""
        # Obtener propiedades actuales
        voices = self.engine.getProperty('voices')
        
        # Configurar velocidad (palabras por minuto)
        self.engine.setProperty('rate', 150)
        
        # Configurar volumen (0.0 a 1.0)
        self.engine.setProperty('volume', 0.9)
        
        # Configurar voz en español 
        for voice in voices:
            if 'spanish' in voice.name.lower() or 'español' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
    
    def texto_a_voz(self, texto):
        """
        Convierte texto a voz y lo reproduce
        Args:
            texto (str): Texto a convertir en voz
        """
        if not texto or texto.strip() == "":
            print("El texto está vacío. Por favor ingrese un texto válido.")
            return
        
        print(f"\n Reproduciendo: '{texto}'")
        self.engine.say(texto)
        self.engine.runAndWait()
        print(" Reproducción completada")
    
    def guardar_audio(self, texto, archivo_salida):
        """
        Guarda el texto como archivo de audio
        Args:
            texto (str): Texto a convertir
            archivo_salida (str): Ruta del archivo de salida
        """
        print(f"\n Guardando audio en: {archivo_salida}")
        self.engine.save_to_file(texto, archivo_salida)
        self.engine.runAndWait()
        print(" AUDIO GUARDADO EXITOSAMENTE")


def menu_sintesis():
    """Menú para la funcionalidad de síntesis de voz"""
    sintesis = SintesisVoz()
    
    while True:
        print("\n" + "="*60)
        print(" SÍNTESIS DE VOZ (Text-to-Speech)")
        print("="*60)
        print("1. Ingresar texto para reproducir")
        print("2. Guardar texto como archivo de audio")
        print("3. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            texto = input("\nIngresa el texto a reproducir: ").strip()
            if texto:
                sintesis.texto_a_voz(texto)
            else:
                print("No se ingresó ningún texto")
        
        elif opcion == "2":
            texto = input("\nIngresa el texto a guardar: ").strip()
            if texto:
                archivo = input("Nombre del archivo (sin extensión): ").strip()
                if not archivo:
                    archivo = "salida"
                archivo_salida = f"{archivo}.mp3"
                sintesis.guardar_audio(texto, archivo_salida)
            else:
                print("No se ingresó ningún texto")
        
        elif opcion == "3":
            break
        
        else:
            print("Opción inválida")

