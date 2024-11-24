import streamlit as st
import qrcode

filename= "qr_code/qr_code.png"

def generate_qr_code(url, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color ="white")
    img.save(file_name)


#Create Streamlit Page

st.set_page_config(page_title="QR Code Generator", page_icon="/", layout="centered")
#st.image("",use_column_width=True)
st.title("QR Code Generator")

url= st.text_input("Enter the URL")

if st.button("Generate QR Code"):
    generate_qr_code(url,filename)
    st.image(filename, use_column_width= True)
    with open(filename, "rb") as f:
                    image_data = f.read()
    download = st.download_button_label(label= "DOwnload QR", data=image_data, file_name = "qr_generated.png")