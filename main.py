
import sys
sys.path.append('/path/to/ffmpeg')

from ffmpegHelper import call_ffmpeg
from gCloudHelper import text_to_mp3


def merge_audio(audio_file1, audio_file2, output_file, vol1=1.0, vol2=1.0):
    """Merges two audios into one. option to adjust volumes for both audio"""
    call_ffmpeg(f'ffmpeg -i {audio_file1} -i {audio_file2} -filter_complex [0:0]volume={vol1}[a];[1:0]volume={vol2}[b];[a][b]amix=inputs=2:duration=shortest -c:a libmp3lame {output_file}', verbose=True)


def make_audio(text, option, pitch, speaking_rate):
    voice = "en-US-Wavenet-F"
    pitch = float(pitch)
    speaking_rate = float(speaking_rate)
    option = int(option)

    text_to_mp3(voice, text, pitch, speaking_rate)

    background_sounds ={
        1: "background_music/birds_chirp.mp3",
        2: "background_music/meditation.mp3",
        3: "background_music/nature_walk.mp3",
        4: "background_music/rain.mp3"}

    #background_sound = "background_music/meditation.mp3"

    merge_audio("en-US-Wavenet-F.mp3", background_sounds[option], "output/final.mp3", vol1=1.0, vol2=2.0)
