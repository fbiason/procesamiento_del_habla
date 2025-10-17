from sintesis import SintesisVoz, menu_sintesis
from reconocimiento import menu_reconocimiento
from crear_ejemplo import crear_audio_ejemplo

def main():
    """Función principal del programa"""
    print("="*60)
    print("  PROGRAMA DE SÍNTESIS Y RECONOCIMIENTO DE VOZ")
    print("="*60)
    print("Actividad Clase 8 - Procesamiento del Habla")
    
    while True:
        print("\n" + "="*60)
        print("MENÚ PRINCIPAL")
        print("="*60)
        print("1. Síntesis de Voz (Text-to-Speech)")
        print("2. Reconocimiento de Voz (Speech-to-Text)")
        print("3. Crear archivo de audio de ejemplo")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            menu_sintesis()
        
        elif opcion == "2":
            menu_reconocimiento()
        
        elif opcion == "3":
            crear_audio_ejemplo()
        
        elif opcion == "4":
            print("\n ¡Nos vemos!")
            break
        
        else:
            print(" Opción inválida. Por favor seleccione 1, 2, 3 o 4")

if __name__ == "__main__":
    main()
