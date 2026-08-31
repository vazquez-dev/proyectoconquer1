# 1. Texto a Voz
# La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible
# en formato mp3. Para ello puedes hacer uso de bibliotecas existenes como nltk (kit de
# herramientas de lenguaje natural), newspaper3k y gtts (puedes seguir las instrucciones de
# instalación de pip).
# Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para
# luego manejar la conversión de texto a voz.
from gtts import gTTS
import os

def texto_a_voz_online(texto, idioma='es', nombre_archivo='salida.mp3'):
    # Crear el objeto de audio
    tts = gTTS(text=texto, lang=idioma, slow=False)
    
    # Guardar el archivo mp3
    tts.save(nombre_archivo)
    print(f"Audio guardado exitosamente como '{nombre_archivo}'")

# Ejemplo de uso
mi_texto = "¡Hola! Este es un ejemplo de conversión de texto a voz usando Python y gTTS."
texto_a_voz_online(mi_texto)