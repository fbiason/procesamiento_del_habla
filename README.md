## Actividad Clase 8 - Procesamiento del Habla
**Síntesis y Reconocimiento de Voz**

- Alumno: Biason Franco
- Materia: Procesamiento del Habla
- Centro Politécnico Malvinas Argentinas - 2025

- Actividad Clase 8:
Este programa implementa dos funcionalidades principales:
1. **Síntesis de Voz (Text-to-Speech)** - 50%
2. **Reconocimiento de Voz (Speech-to-Text)** - 50%

---

## 📋 Requisitos

### Dependencias de Python
- `pyttsx3==2.90` - Motor de síntesis de voz
- `SpeechRecognition==3.10.0` - Reconocimiento de voz
- `PyAudio==0.2.14` - Captura de audio desde micrófono (opcional)

### Requisitos del Sistema
- **Python 3.7+**
- **Windows**: Viene con soporte de voz integrado
- **Conexión a Internet**: Necesaria para el reconocimiento de voz (usa Google Speech Recognition)

---

## 🚀 Instalación

### 1. Crear entorno virtual (recomendado)
```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Instalación de PyAudio en Windows (si hay problemas)
Si `pip install PyAudio` falla, descargue el wheel apropiado desde:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

Luego instale:
```bash
pip install PyAudio‑0.2.14‑cp3XX‑cp3XX‑win_amd64.whl
```
(Reemplace `3XX` con su versión de Python, ej: `311` para Python 3.11)

---

## 💻 Uso del Programa

### Ejecutar el programa principal
```bash
python main.py
```

### Menú Principal
El programa presenta un menú interactivo con las siguientes opciones:

```
1. Síntesis de Voz (Text-to-Speech)
2. Reconocimiento de Voz (Speech-to-Text)
3. Crear archivo de audio de ejemplo
4. Salir
```

## Síntesis de Voz (50%)

### Funcionalidades
1. **Reproducir texto**: Ingresa texto y el programa lo convierte a voz
2. **Guardar como audio**: Guarda el texto como archivo de audio (MP3)

### Características
- Velocidad ajustable (150 palabras por minuto por defecto)
- Volumen configurable (0.9 por defecto)
- Soporte para voces en español (si están disponibles en el sistema)
- Interfaz interactiva y amigable

### Ejemplo de uso
```
Ingrese el texto a reproducir: Hola, este es un ejemplo de síntesis de voz
Reproduciendo: 'Hola, este es un ejemplo de síntesis de voz'
Reproducción completada
```

---

## 🎤 Reconocimiento de Voz (50%)

### Funcionalidades
1. **Convertir archivo WAV a texto**: Procesa archivos de audio WAV existentes
2. **Grabar desde micrófono**: Graba audio en tiempo real y lo convierte a texto

### Características
- Soporte para múltiples idiomas (español e inglés por defecto)
- Ajuste automático para ruido ambiente
- Procesamiento de archivos WAV
- Grabación desde micrófono con duración configurable

### Ejemplo de uso con archivo WAV
```
(me grabe en un audio de whatsapp, lo descargue en la computadora y lo convertí a .wav con convertio.co)
Ingrese la ruta del archivo WAV: actividad_8.wav 
Procesando archivo: actividad_8.wav
Reconociendo voz...
Texto reconocido: 'Buen día mi nombre es Franco villazón y esta actividad número 8 desplazamiento del habla'
(mi apellido es Biasón, pero el reconocimiento lo interpreto como "villazón")
```

### Ejemplo de uso con micrófono
```
- Duración de grabación en segundos [5]: 5
- Grabando desde el micrófono por 5 segundos...
- Ajustando para ruido ambiente...
- Habla ahora...
- Reconociendo voz...
- Texto reconocido: no me reconocio ningún texto. Me salto el "Error: No module named 'distutils'"
```

---

## Crear Archivo de Ejemplo

### Opción 1: Desde el menú principal
Seleccione la opción 3 en el menú principal para crear automáticamente un archivo de audio de ejemplo.

### Opción 2: Script independiente
```bash
python ejemplo.py
```

Este script crea un archivo de audio con el texto:
> "Hola, este es un ejemplo de reconocimiento de voz en español. Procesamiento del habla."

**Nota**: Dependiendo de la plataforma, puede crear un archivo MP3 en lugar de WAV. Use FFmpeg o Audacity para convertir:
```bash
ffmpeg -i ejemplo.mp3 ejemplo.wav
```

---

## 📁 Estructura del Proyecto

```
actividad_clase8_pdh/
│
├── main.py                 # Programa principal (menú y coordinación)
├── sintesis.py             # Módulo de síntesis de voz (SintesisVoz + menu_sintesis)
├── reconocimiento.py       # Módulo de reconocimiento de voz (ReconocimientoVoz + menu_reconocimiento)
├── crear_ejemplo.py        # Script para crear archivos de audio de ejemplo
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
│
└── (archivos generados)
    ├── ejemplo_creado.mp3 # Archivo de audio de ejemplo generado
    └── actividad_8.wav    # Archivo de audio para pruebas de reconocimiento
```

---

## 🎯 Funcionalidades Implementadas

### ✅ Síntesis de Voz (50%)
- [x] Conversión de texto a voz usando `pyttsx3`
- [x] Entrada interactiva de texto por parte del usuario
- [x] Reproducción de audio en tiempo real
- [x] Guardado de audio como archivo
- [x] Configuración de velocidad y volumen
- [x] Soporte para voces en español

### ✅ Reconocimiento de Voz (50%)
- [x] Conversión de audio WAV a texto usando `SpeechRecognition`
- [x] Procesamiento de archivos WAV existentes
- [x] Grabación desde micrófono
- [x] Ajuste automático para ruido ambiente
- [x] Soporte multiidioma (español/inglés)
- [x] Archivo WAV de ejemplo incluido

---

### Error al instalar PyAudio
- **Windows**: Descargue el wheel desde https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
- **Linux**: `sudo apt-get install portaudio19-dev python3-pyaudio`
- **macOS**: `brew install portaudio && pip install pyaudio`

### Error: "No se pudo entender el audio"
- Verifique que el archivo WAV contenga audio claro
- Asegúrese de que el audio esté en un idioma soportado
- Intente con un archivo de mejor calidad

### Error: "Error en el servicio de reconocimiento"
- Verifique su conexión a Internet
- El servicio de Google Speech Recognition requiere conectividad

---

## 📚 Tecnologías Utilizadas

- **pyttsx3**: Motor de síntesis de voz multiplataforma
- **SpeechRecognition**: Biblioteca para reconocimiento de voz
- **PyAudio**: Captura de audio desde micrófono
- **Google Speech Recognition API**: Servicio de reconocimiento de voz en la nube

---


## 📝 Notas Adicionales

- El reconocimiento de voz requiere conexión a Internet (usa Google Speech Recognition API)
- La calidad del reconocimiento depende de la claridad del audio
- Para mejores resultados, use archivos WAV con buena calidad de grabación
- El programa soporta español (es-ES) e inglés (en-US) por defecto
- Se pueden agregar más idiomas modificando el parámetro `language` en las funciones de reconocimiento

---