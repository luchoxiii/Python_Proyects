import pyshorteners
import streamlit as st

## Les Champs-Elysess by Joe Dassin

def shorten_url(url):
    s = pyshorteners.shortener()
    shorten_url = s.tinyurl.short(url)
    return shorten_url

#Creacion de la app web con streamlit

st.set_page_config(page_title="URL Shortener", page_icon="/", layout="centered")
#st.image("",use_column_width=True)
st.title("URL Shortener")

url= st.text_input("Enter the URL")

if st.button("Generate new URL"):
    st.write("URL shortened: ",shorten_url(url))
