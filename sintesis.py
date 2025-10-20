import pyttsx3

class SintesisVoz:
    """Como manejar la síntesis de voz (Text-to-Speech)"""
    
    def __init__(self):
        """Inicializa el motor de síntesis de voz"""
        try:
            self.engine = pyttsx3.init()
            self._configurar_motor()
        except Exception as e:
            print(f"⚠️  Error al inicializar el motor de síntesis: {e}")
            print("🔄 Intentando inicializar con driver específico...")
            try:
                self.engine = pyttsx3.init('sapi5')  # Driver para Windows
                self._configurar_motor()
            except Exception as e2:
                print(f"❌ Error crítico: {e2}")
                raise
    
    def _configurar_motor(self):
        """Configura las propiedades del motor de voz"""
        try:
            # Obtener propiedades actuales
            voices = self.engine.getProperty('voices')
            
            # Configurar velocidad (palabras por minuto)
            self.engine.setProperty('rate', 150)
            
            # Configurar volumen (0.0 a 1.0)
            self.engine.setProperty('volume', 0.9)
            
            # Configurar voz en español 
            voz_encontrada = False
            for voice in voices:
                if 'spanish' in voice.name.lower() or 'español' in voice.name.lower():
                    self.engine.setProperty('voice', voice.id)
                    voz_encontrada = True
                    print(f"✅ Voz en español configurada: {voice.name}")
                    break
            
            if not voz_encontrada and voices:
                # Si no hay voz en español, usar la primera disponible
                self.engine.setProperty('voice', voices[0].id)
                print(f"⚠️  No se encontró voz en español. Usando: {voices[0].name}")
        except Exception as e:
            print(f"⚠️  Advertencia al configurar el motor: {e}")
            print("🔄 Continuando con configuración por defecto...")
    
    def texto_a_voz(self, texto):
        """
        Convierte texto a voz y lo reproduce
        Args:
            texto (str): Texto a convertir en voz
        """
        if not texto or texto.strip() == "":
            print("⚠️  El texto está vacío. Por favor ingrese un texto válido.")
            return
        
        try:
            print(f"\n🔊 Reproduciendo: '{texto}'")
            self.engine.say(texto)
            self.engine.runAndWait()
            print("✅ Reproducción completada")
        except Exception as e:
            print(f"❌ Error al reproducir el audio: {e}")
            print("🔧 Verifica que los drivers de audio estén funcionando correctamente.")
    
    def guardar_audio(self, texto, archivo_salida):
        """
        Guarda el texto como archivo de audio
        Args:
            texto (str): Texto a convertir
            archivo_salida (str): Ruta del archivo de salida
        """
        try:
            print(f"\n💾 Guardando audio en: {archivo_salida}")
            self.engine.save_to_file(texto, archivo_salida)
            self.engine.runAndWait()
            print("✅ AUDIO GUARDADO EXITOSAMENTE")
        except Exception as e:
            print(f"❌ Error al guardar el audio: {e}")
            print("🔧 Verifica que tengas permisos de escritura en el directorio.")


def menu_sintesis():
    """Menú para la funcionalidad de síntesis de voz"""
    try:
        sintesis = SintesisVoz()
    except Exception as e:
        print(f"\n❌ Error al inicializar el sistema de síntesis de voz: {e}")
        print("🔧 Verifica que pyttsx3 esté instalado correctamente.")
        print("💡 Puedes intentar reinstalarlo con: pip install --upgrade pyttsx3")
        input("\n⏎ Presiona Enter para volver al menú principal...")
        return
    
    while True:
        print("\n" + "="*60)
        print("🔊 SÍNTESIS DE VOZ (Text-to-Speech)")
        print("="*60)
        print("1. 🎤 Ingresar texto para reproducir")
        print("2. 💾 Guardar texto como archivo de audio")
        print("3. ⬅️  Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            texto = input("\n📝 Ingresa el texto a reproducir: ").strip()
            if texto:
                sintesis.texto_a_voz(texto)
            else:
                print("⚠️  No se ingresó ningún texto")
        
        elif opcion == "2":
            texto = input("\n📝 Ingresa el texto a guardar: ").strip()
            if texto:
                archivo = input("📁 Nombre del archivo (sin extensión): ").strip()
                if not archivo:
                    archivo = "salida"
                archivo_salida = f"{archivo}.mp3"
                sintesis.guardar_audio(texto, archivo_salida)
            else:
                print("⚠️  No se ingresó ningún texto")
        
        elif opcion == "3":
            print("👋 Volviendo al menú principal...")
            break
        
        else:
            print("❌ Opción inválida")

