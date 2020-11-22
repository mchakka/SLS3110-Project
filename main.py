
import gtts
import os

# make request to google to get synthesis
def function(mytext):

    language = 'en'

    myobj = gtts.gTTS(text=mytext, lang=language, slow=False)

    myobj.save("audio_file.mp3")

if __name__ == '__main__':
    text = "I love this amazing class"
    function(text)
