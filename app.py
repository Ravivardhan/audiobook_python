import imghdr
import os

import flask

from flask import Flask, render_template, request, flash, url_for
from werkzeug.utils import secure_filename, redirect
import PyPDF4 as PyPDF2
import pyttsx3
speaker = pyttsx3.init()
import pyrebase
from gtts import gTTS
import os
from playsound import playsound
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key='audiobook'

firebaseConfig = {
    'apiKey': "AIzaSyDKdjZCX083VYr4a1cb7pIhWiRvOrJkFwo",
    'authDomain': "audiobook-68661.firebaseapp.com",
    'projectId': "audiobook-68661",
    'storageBucket': "audiobook-68661.appspot.com",
    'messagingSenderId': "915447668878",
    'appId': "1:915447668878:web:536efc64c13b5fc6d9a9df",
    'measurementId': "G-8943FX49PW",
    'databaseURL':"https://audiobook-68661-default-rtdb.firebaseio.com/"
  }

firebase=pyrebase.initialize_app(firebaseConfig)


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
    print(title)
    if '/Title' not in title:
        title="this document does not contain any title"

    # title of the pdf here///
    else:
        title=title['/Title']




    tts = gTTS(text=title, lang='it')
    tts.save("title.mp3")
    mytext=""
    for page_num in range(1,pdfReader.numPages):
        pageObj=pdfReader.getPage(page_num)
        mytext+=pageObj.extractText()+'\n'
    print(mytext)
    if mytext=="":
        mytext="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>cannot parse</title>
</head>
<body>
    <h1>No text found try another one!!!</h1>
    
</body>
</html>"""
        return mytext
    text=mytext
    myobj=gTTS(text=text,lang='en',slow=False)
    myobj.save('static/ab.mp3')
    playsound("title.mp3")

    #tts=gTTS(text=mytext,lang='en')
    #tts.save('story.mp3')
    #speaker.save_to_file(text,'audiobook.mp3')
    return render_template('audiobook.html')




    #sst=gTTS(text=text,lang='en')
    #sst.save("content.mp3")
    #playsound("audiobook.mp3")

@app.route('/notes',methods=['POST','GET'])
def notes():
        print(request.method)
        if request.method=='POST':
            print("nothinh")
            text=request.form.get('addnote')
            print(text)
            file=open('notes/mynotes.txt','a')
            file.write('\n'+text)
        return render_template('audiobook.htmml')


@app.route("/test", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        todo = request.form.get("todo")
        file=open('notes/mynotes.txt','a')
        #date timestamp
        from datetime import datetime

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        file.write('\n'+current_time)
        file.write('\n'+todo)
        file.close()
    return render_template('audiobook.html')
@app.route('/file',methods=["POST","GET"])
def file():
    f = open('notes/mynotes.txt', "r")
    sample = f.read()
    return render_template("file.html", text=sample)


if __name__ == '__main__':
    app.run()
    app.debug=True