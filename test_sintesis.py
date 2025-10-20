"""Script de prueba para verificar que la síntesis de voz funciona correctamente"""
from sintesis import SintesisVoz

def test_sintesis():
    print("="*60)
    print("🧪 PRUEBA DE SÍNTESIS DE VOZ")
    print("="*60)
    
    try:
        # Inicializar el motor
        print("\n1️⃣  Inicializando motor de síntesis...")
        sintesis = SintesisVoz()
        print("✅ Motor inicializado correctamente\n")
        
        # Probar reproducción de texto
        print("2️⃣  Probando reproducción de texto...")
        texto_prueba = "Hola, esta es una prueba de síntesis de voz"
        sintesis.texto_a_voz(texto_prueba)
        
        # Probar guardar audio
        print("\n3️⃣  Probando guardar audio...")
        sintesis.guardar_audio("Prueba de guardado de audio", "test_output.mp3")
        
        print("\n" + "="*60)
        print("🎉 TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ ERROR EN LAS PRUEBAS: {e}")
        print("\n💡 Posibles soluciones:")
        print("1. 🔄 Reinstala pyttsx3: pip install --upgrade pyttsx3")
        print("2. 📦 Instala pywin32: pip install pywin32")
        print("3. 🔊 Verifica que los drivers de audio estén funcionando")

if __name__ == "__main__":
    test_sintesis()
