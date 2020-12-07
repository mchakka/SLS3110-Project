
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
from temp2 import text_to_mp3


def merge_audio(audio_file1, audio_file2, output_file, vol1=1.0, vol2=1.0):
    """Merges two audios into one. option to adjust volumes for both audio"""
    call_ffmpeg(f'ffmpeg -i {audio_file1} -i {audio_file2} -filter_complex [0:0]volume={vol1}[a];[1:0]volume={vol2}[b];[a][b]amix=inputs=2:duration=shortest -c:a libmp3lame {output_file}', verbose=True)


if __name__ == '__main__':
    text = "The Greening Youth Foundation’s mission is to engage under-represented youth and young adults,"
    speaking_rate = 0.85
    pitch = 0
    voice = "en-US-Wavenet-F"

    text_to_mp3(voice, text,pitch, speaking_rate)

    background_sounds ={
        1: "background_music/birds_chirp.mp3",
        2: "background_music/meditation.mp3",
        3: "background_music/nature_walk.mp3",
        4: "background_music/rain.mp3"}

    #background_sound = "background_music/meditation.mp3"

    merge_audio("en-US-Wavenet-F.mp3", background_sounds[1], "mixed.mp3", vol1=1.0, vol2=2.0)
