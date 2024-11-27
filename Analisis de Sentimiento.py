#Analisis de Sentimiento
#Lucho Nov|2022
#Happy Ground by Pete Murray

from textblob import TextBlob 

def analyze_sentiment(text):
    blob = TextBlob(text)  

    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positivo"
    elif polarity < 0:
        sentiment = "Negativo"
    else:
        sentiment = "Neutro"

    print(f"Texto: {text}")
    print(f"Polaridad: {polarity}")
    print(f"Sentimiento: {sentiment}")


text_example = "I hate you"
analyze_sentiment(text_example)
