import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import re

# Creamos una funcion que transforme el texto a voz
def texto_a_voz(texto, idioma='es', nombre_archivo='audio_texto.mp3'):
    # Creamos el objeto de audio
    tts = gTTS(text=texto, lang=idioma, slow=False)
    
    # Guardarmos el archivo mp3
    tts.save(nombre_archivo)
    print(f"Audio guardado exitosamente como '{nombre_archivo}'")

# HACEMOS WEB SCRAPPING ESTATICO PARA PROYECTO TEXTO A VOZ

# Descargamos una noticia de una pagina web y guardamos su contenido en el disco
url ="https://www.infobae.com/economia/2026/08/31/g20-de-estados-unidos-comenzo-el-encuentro-de-ministros-de-economia-y-caputo-se-reunira-con-el-secretario-del-tesoro-scott-bessent/"
try:
    page = requests.get(url)
except:
     print("Error al abrir url")

# Luego de hacer el requests parseamos el contenido de HTML usando html.parser
# Parseamos el htlm usando BS y lo guardamos en la variable soup
soup = BeautifulSoup(page.text, 'html.parser')

# Buscamos el cuerpo del html en el elemento <div>. En este caso -> soup.find('div', {"class":"body-article"})
frases = soup.find('div', {"class":"body-article"})

# Metemos el texto dentro de una lista
articulo = []
for i in frases.find_all('p'):
    articulo.append(i.text)
print('\n'.join(articulo))

# Convertimos articulo a str para luego poder pasar el texto a voz
texto_final = str(articulo)
print(texto_final)

# Llamamos a la funcion para convertir el texto extraido a voz
texto_a_voz(texto_final)

#------------------------------------------------------------------------------

# OPCIONAL - Guardar el texto en un archivo.txt
guardar_texto = input(f"Deseas guardar el contenido en un archivo.txt: 1-Si 2-No ")
if guardar_texto == "1":
    with open("archivo.txt", "w", encoding="utf-8") as f:
        f.write(texto_final)
        print("Archivo de texto creado exitosamente")
else:
    print("Fin del proceso de conversión")
