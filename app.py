from flask import Flask, render_template, request
from flask import send_file
import main

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/convert', methods=['GET', 'POST'])
def convert():
    actaulText = request.form['temp'] # text from a form submit
    number = request.form['temp2']
    pitch = request.form['pitch']
    rate = request.form['rate']

    print("text " + actaulText)
    print("option " + number)
    print("pitch " + pitch)
    print("rate " + rate)

    file = main.make_audio(actaulText, number, pitch, rate) #Inan's work

    #returns an mp3 file

    return send_file("output/final.mp3", as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)