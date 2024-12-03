# pip install gTTS

from ggts import gTTS

archivo = open("libro.txt","r", encoding="utf-8" )
texto = archivo.read()
archivo.close()

#Je ne sais pas by Joyce Jonathan

tts = gTTS(text = texto, lang="es")
tts.save("audio_libro.mp3")