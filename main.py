
import gtts
import os
from pydub import AudioSegment
import sys
sys.path.append('/path/to/ffmpeg')

import os
import uuid
import shutil
import subprocess
from shared_lib import call_ffmpeg, get_duration


# make request to google to get synthesis

def merge_audio(audio_file1, audio_file2, output_file, vol1=1.0, vol2=1.0):
    """Merges two audios into one. option to adjust volumes for both audio"""
    call_ffmpeg(f'ffmpeg -i {audio_file1} -i {audio_file2} -filter_complex [0:0]volume={vol1}[a];[1:0]volume={vol2}[b];[a][b]amix=inputs=2:duration=longest -c:a libmp3lame {output_file}', verbose=True)

def function(mytext):

    language = 'en'

    myobj = gtts.gTTS(text=mytext, lang=language, slow=False)

    myobj.save("audio_file.mp3") #temp comment

    # sound1 = AudioSegment.from_mp3("audio_file.mp3")
    # sound2 = AudioSegment.from_mp3("birds_chirp.mp3")
    #
    # # mix sound2 with sound1, starting at 5000ms into sound1)
    # output = sound1.overlay(sound2, position=5000)
    #
    # # save the result
    # output.export("mixed_sounds.mp3", format="mp3")

if __name__ == '__main__':
    text = "I love this amazing class"
    function(text)
    merge_audio("audio_file.mp3", "birds_chirp.mp3", "mixed.mp3", vol1=1.0, vol2=1.0)
