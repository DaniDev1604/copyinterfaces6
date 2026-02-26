import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.title("Conversión de Texto a Audio")
image = Image.open('telefono.jpeg')
st.image(image, width=350)
with st.sidebar:
    st.subheader("Esrcibe y/o selecciona texto para ser escuchado.")


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Una pequeña Fábula.")

st.write(' Una adolescente está cuidando por primera vez a unos niños en una casa enorme y lujosa. Acuesta a los niños en el piso de arriba, y, cuando apenas se ha sentado delante de la televisión, suena el teléfono.' 
         ' A juzgar por su voz, el que llama es un hombre. Jadea, ríe de forma amenazadora y pregunta: “¿Has subido a ver a los niños?”.'  
         ' La chica cuelga convencido de que sus amigos le están gastando una broma, pero el hombre vuelve a llamar y pregunta de nuevo: “¿Has subido a ver a los niños?”.' 
         ' Ella cuelga a toda prisa, pero el hombre llama por tercera vez, y esta vez dice: “¡Ya me he ocupado de los niños, ahora voy a por ti!”.'
         ' La chica está verdaderamente asustada. Llama a la policía y denuncia las llamadas amenazadoras. La policía pide que, si vuelve a llamar, intente distraerle al teléfono para que les de tiempo a localizar la llamada.'
         ' Como era de esperar, el hombre llama de nuevo a los pocos minutos. La chica le suplica que la deje en paz, y así le entretiene. Él acaba por colgar. De repente, el teléfono suena de nuevo, y a cada timbrazo el tono es más alto y más estridente.'
         ' En esta ocasión, es la policía, que le da una orden urgente: “¡Salga de la casa inmediatamente! ¡Las llamadas vienen del piso de arriba!”.')
           
st.markdown(f"Quieres escucharlo?, copia el texto")
text = st.text_area("Ingrese El texto a escuchar.")

tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'

def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir a Audio"):
     result, output_text = text_to_speech(text, 'com',lg)#'tld
     audio_file = open(f"temp/{result}.mp3", "rb")
     audio_bytes = audio_file.read()
     st.markdown(f"## Tú audio:")
     st.audio(audio_bytes, format="audio/mp3", start_time=0)

     #if display_output_text:
     
     #st.write(f" {output_text}")
    
#if st.button("ElevenLAabs",key=2):
#     from elevenlabs import play
#     from elevenlabs.client import ElevenLabs
#     client = ElevenLabs(api_key="a71bb432d643bbf80986c0cf0970d91a", # Defaults to ELEVEN_API_KEY)
#     audio = client.generate(text=f" {output_text}",voice="Rachel",model="eleven_multilingual_v1")
#     audio_file = open(f"temp/{audio}.mp3", "rb")

     with open(f"temp/{result}.mp3", "rb") as f:
         data = f.read()

     def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
     st.markdown(get_binary_file_downloader_html("audio.mp3", file_label="Audio File"), unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
