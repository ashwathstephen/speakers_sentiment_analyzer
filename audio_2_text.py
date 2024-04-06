# import os
# import json
# from dotenv import load_dotenv
# from deepgram import (
#     DeepgramClient,
#     PrerecordedOptions,
#     FileSource,
# )
# load_dotenv()
# API_KEY = os.getenv("DG_API_KEY")
# deepgram = DeepgramClient(api_key=API_KEY)

# AUDIO_FILE = "spacewalk.mp3"

# options = PrerecordedOptions(
#     punctuate= True,
#     diarize= True,
# )

# def main():
#     with open(AUDIO_FILE, "rb") as f:
#         source = {"buffer": f.read()}
#         res = deepgram.listen.prerecorded.v("1").transcribe_file(source, options)
#         with open(f"./{AUDIO_FILE[:-4]}.json", "w") as transcript:
#             json.dump(res.to_json(),transcript,indent=4)
#     return

# # main()
# TAG = 'SPEAKER_'

# def create_transcript(output_json, output_transcript):
#   lines = []
#   with open(output_json, "r") as file:
#     words = json.loads(json.load(file))["results"]["channels"][0]["alternatives"][0]["words"]
#     curr_speaker = 0
#     curr_line = ''
#     for word_struct in words:
#       word_speaker = word_struct["speaker"]
#       word = word_struct["punctuated_word"]
#       if word_speaker == curr_speaker:
#         curr_line += ' ' + word
#       else:
#         tag = TAG + str(curr_speaker) + ':'
#         full_line = tag + curr_line + '\n'
#         curr_speaker = word_speaker
#         lines.append(full_line)
#         curr_line = ' ' + word
#     lines.append(TAG + str(curr_speaker) + ':' + curr_line)
#     with open(output_transcript, 'w') as f:
#       for line in lines:
#         f.write(line)
#         f.write('\n')
#   return

# create_transcript('spacewalk.json', 'spacewalk.txt')


import os
from dotenv import load_dotenv
from deepgram import DeepgramClient, PrerecordedOptions

load_dotenv()
API_KEY = os.getenv("DEEPGRAM_API_KEY")
deepgram = DeepgramClient(api_key="40628bbe8b195fd017e2d592b4242ade10f1186d")

TAG = 'SPEAKER '

def audio_to_text(audio_file):
    options = PrerecordedOptions(
        punctuate=True,
        diarize=True,
    )

    # with open(audio_file, "rb") as f:
    source = {"buffer": audio_file}
    res = deepgram.listen.prerecorded.v("1").transcribe_file(source, options)

    words = res["results"]["channels"][0]["alternatives"][0]["words"]
    lines = []
    curr_speaker = 0
    curr_line = ''

    for word_struct in words:
        word_speaker = word_struct["speaker"]
        word = word_struct["punctuated_word"]

        if word_speaker == curr_speaker:
            curr_line += ' ' + word
        else:
            tag = TAG + str(curr_speaker) + ':'
            full_line = tag + curr_line + '\n'
            lines.append(full_line)
            curr_speaker = word_speaker
            curr_line = ' ' + word

    lines.append(TAG + str(curr_speaker) + ':' + curr_line)
    speaker_dict = {}
    for i in lines:
        curr_speaker = i.split(':')[0]
        speaker_dict.setdefault(curr_speaker,'')
        speaker_dict[curr_speaker]+=(i[len(curr_speaker)+1:])
    return speaker_dict, lines

# audio_to_text("spacewalk.mp3")
