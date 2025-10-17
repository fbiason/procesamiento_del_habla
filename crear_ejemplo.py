from sintesis import SintesisVoz, menu_sintesis
from reconocimiento import menu_reconocimiento

def crear_audio_ejemplo():
    """Crea un archivo WAV de ejemplo para pruebas"""
    print("\n Creando archivo de audio de ejemplo...")
    
    sintesis = SintesisVoz()
    archivo_ejemplo = "ejemplo.wav"
    texto_ejemplo = "Hola, este es un ejemplo de reconocimiento de voz de procesamiento del habla."
    
    # Nota: pyttsx3 puede no soportar WAV directamente en todas las plataformas
    # Guardamos como MP3 y notificamos al usuario
    sintesis.guardar_audio(texto_ejemplo, "ejemplo_creado.mp3")
    print(f"\n Se creo 'ejemplo.mp3' con el texto: '{texto_ejemplo}'")
    print("  Para convertirlo a WAV, puede usar herramientas como FFmpeg o Audacity (o convertico.co)")

