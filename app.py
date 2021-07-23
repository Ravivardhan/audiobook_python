import imghdr
import os
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename, redirect
import PyPDF2
import pyttsx3
speaker = pyttsx3.init()
from gtts import gTTS
import os
from playsound import playsound
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
    title=pdfReader.getDocumentInfo()
    text=""

    # title of the pdf here///
    print(title['/Title'])


    tts = gTTS(text=title['/Title'], lang='it')
    tts.save("title.mp3")
    playsound("title.mp3")

    for page_num in range(pdfReader.numPages):
        text += pdfReader.getPage(page_num).extractText()

    speaker.say(text)
    print(text)
    speaker.runAndWait()
    speaker.stop()
    #speaker.save_to_file(text,'audiobook.mp3')




    #sst=gTTS(text=text,lang='en')
    #sst.save("content.mp3")
    #playsound("audiobook.mp3")


if __name__ == '__main__':
    app.run()
    app.debug=True