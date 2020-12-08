from google.cloud import texttospeech
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"


def list_voices(language_code=None):
    client = texttospeech.TextToSpeechClient()
    response = client.list_voices(language_code=language_code)
    voices = sorted(response.voices, key=lambda voice: voice.name)

    print(f" Voices: {len(voices)} ".center(60, "-"))
    for voice in voices:
        languages = ", ".join(voice.language_codes)
        name = voice.name
        gender = texttospeech.SsmlVoiceGender(voice.ssml_gender).name
        rate = voice.natural_sample_rate_hertz
        print(f"{languages:<8} | {name:<24} | {gender:<8} | {rate:,} Hz")

# https://googleapis.dev/python/texttospeech/latest/gapic/v1beta1/types.html#google.cloud.texttospeech_v1beta1.types.AudioConfig
# this is to change the pitch, speaking speed etc...
# speaking_rate is between 0.25 and 4
# pitch is between in the range [-20.0, 20.0]

def text_to_mp3(voice_name, text, pitch, speaking_rate):
    language_code = "-".join(voice_name.split("-")[:2])
    text_input = texttospeech.SynthesisInput(text=text)
    voice_params = texttospeech.VoiceSelectionParams(language_code=language_code, name=voice_name)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3,pitch = pitch,speaking_rate = speaking_rate )

    client = texttospeech.TextToSpeechClient()
    response = client.synthesize_speech(
        input=text_input, voice=voice_params, audio_config=audio_config
    )

    filename = f"{voice_name}.mp3"
    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to "{filename}"')

# def final(voice, text,pitch, speaking_rate):    #list_voices("en-US")
#
#     text_to_mp3(voice, text,pitch, speaking_rate)
#



