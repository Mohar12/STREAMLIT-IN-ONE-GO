import streamlit as st
import pandas as pd
st.subheader("LOADING OF CSV FILE")
st.subheader("DEALING WITH CSV")
df=st.file_uploader("UPLOAD THE CSV FILE :",type=["csv","xlsx"])

if df is not None:
    st.dataframe(df);

df=pd.read_csv("Products.csv")
if df is not None:
    st.table(df.head())

st.subheader("DEALING WITH IMAGES")
img=st.file_uploader("UPLOAD THE IMAGE FILE :",type=["png","jpg"])

if img is not None:
    st.image(img)

st.subheader("DEALING WITH VIDEOS")
video=st.file_uploader("UPLOAD THE VIDEO FILE :",type=["mp4","avi"])
if video is not None:
    st.video(video,start_time=0)

st.subheader("DEALING WITH AUDIOS")

audio=st.file_uploader("UPLOAD THE AUDIO FILE :",type=["mp3"])
if audio is not None:
    st.audio(audio)
