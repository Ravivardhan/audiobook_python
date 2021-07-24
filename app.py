import imghdr
import os

import flask

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
app.secret_key='audiobook'
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
    #title=pdfReader.getDocumentInfo()
    #text=""

    # title of the pdf here///
    #print(title['/Title'])


    #tts = gTTS(text=title['/Title'], lang='it')
    #tts.save("title.mp3")
    #playsound("title.mp3")
    mytext=""
    for page_num in range(1,pdfReader.numPages):
        pageObj=pdfReader.getPage(page_num)
        mytext+=pageObj.extractText()+'\n'
    print(mytext)

    text=mytext
    myobj=gTTS(text=text,lang='en',slow=False)
    myobj.save('static/ab.mp3')
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


if __name__ == '__main__':
    app.run()
    app.debug=True