import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
st.title("YT Transciption Extractor")
flag = 0
text = st.text_input("Enter YouTube Video URL: ")
final = ""
if len(text)>0:
    st.video(text)
    yt = YouTubeTranscriptApi.get_transcript(text.split(sep='/')[-1], languages=['en'])
    if len(yt) > 0:
        for i in yt:
            final += i['text'] + ' '
        st.header('Translated Transcript: ')
        st.write(final)