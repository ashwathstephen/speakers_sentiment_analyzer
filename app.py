import streamlit as st
from htmlTemplates import css
from audio_2_text import audio_to_text
from senti_analysis import analyze_sentiment
from streamlit.components.v1 import html
import streamlit_scrollable_textbox as stx

def process_audio_files(audio_file):
    st.write(f"Processing {audio_file.name}...")
    speakers_dict, transcript = audio_to_text(audio_file)
    text = ""
    for each_speaker in speakers_dict:
        sentiment = analyze_sentiment(speakers_dict[each_speaker])
        text+=f"{each_speaker}: {sentiment}\n\n"
    return text, "\n".join(transcript)

def main():
    st. set_page_config(
        page_title="Speakers sentiment analyzer",
                  layout="wide")
    st.header("Speakers sentiment analyzer")
    st.write(css, unsafe_allow_html=True)
    # st.subheader("Your Audio")
    col1, col2 = st.columns(2)
    with col1:
        audio_file = st.file_uploader("Upload your audio file click on 'Process sentiment'")
    if st.button("Process sentiment"):
        with st.spinner("Processing"):
            if audio_file:
                texts, transcript = process_audio_files(audio_file)
                # st.write("Results:")
                col1, col2 = st.columns(2)
                with col1:
                    st.header("Sentiment")
                    stx.scrollableTextbox(texts,height = 300)

                with col2:
                    st.header("Transcription")
                    stx.scrollableTextbox(transcript,height = 300)
if __name__ == '__main__':
    main()
