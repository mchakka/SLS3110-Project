from flask import Flask, render_template, request
import main

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/convert', methods=['GET', 'POST'])
def convert():
    actaulText = request.form['temp'] # text from a form submit
    number = request.form['number']
    file = main.function(actaulText, number) # Inan's work
    #returns an mp3 file
    return render_template("index.html", output=file)


if __name__ == '__main__':
    app.run(debug=True)