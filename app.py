import imghdr
import os
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename, redirect
import PyPDF2
import pyttsx3
speaker = pyttsx3.init()

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_files():
    if request.method == 'POST':

        file = request.files['file']


        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("saved file successfully")
        return audio(filename)
        # submit an empty part without filename
    return flash("no files selected..")

def audio(file):
    pdfReader = PyPDF2.PdfFileReader(open('uploads/{}'.format(file), 'rb'))
    text = pdfReader.getPage(25).extractText()
    title=pdfReader.getDocumentInfo()

    # title of the pdf here///
    print(title['/Title'])

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(title['/Title'])
    engine.runAndWait()
    speaker.setProperty('voice', voices[1].id)
    speaker.say(text)
    speaker.runAndWait()



if __name__ == '__main__':
    app.run()
    app.debug=True