import streamlit as st
from htmlTemplates import css
from audio_2_text import audio_to_text
from senti_analysis import analyze_sentiment
from streamlit.components.v1 import html
import streamlit_scrollable_textbox as stx
import json

def process_audio_files(audio_file):
    st.write(f"Processing {audio_file.name}...")
    speakers_dict, transcript = audio_to_text(audio_file)
    text = ""
    for each_speaker in speakers_dict:
        sentiment = analyze_sentiment(speakers_dict[each_speaker])
        text += f"{each_speaker}: {sentiment}\n\n"
    return text, "\n".join(transcript)

def main():
    st.set_page_config(page_title="Speakers sentiment analyzer", layout="wide")
    st.header("Speakers sentiment analyzer")
    st.write(css, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        audio_file = st.file_uploader("Upload your audio file click on 'Process sentiment'")
    if st.button("Process sentiment"):
        if audio_file is not None:
            sentiment_text, transcript = process_audio_files(audio_file)
            with col2:
                st.write("## Sentiment Analysis")
                stx.scrollable_textbox(sentiment_text, height=300)
                st.write("## Transcript")
                stx.scrollable_textbox(transcript, height=300)
        else:
            st.error("Please upload a file to process.")

def lambda_handler(event, context):
    # Assuming the event contains an audio file or related data in a suitable format
    audio_data = event.get('audio_data')  # Placeholder for audio data extraction

    # Process the audio data as per the application's logic (needs adaptation based on event structure)
    # speakers_dict, transcript = audio_to_text(audio_data)  # This needs to be adapted to handle data from event
    # text = ""
    # for each_speaker in speakers_dict:
    #     sentiment = analyze_sentiment(speakers_dict[each_speaker])
    #     text += f"{each_speaker}: {sentiment}\n\n"
    
    # Placeholder response (adapt as necessary)
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Function executed successfully!",
            # "sentiment_text": text,
            # "transcript": "\n".join(transcript)
        })
    }

    return response

# Comment out Streamlit's direct execution
# if __name__ == "__main__":
#     main()
