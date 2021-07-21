from gtts import gTTS
import os
from playsound import playsound
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
playsound("good.mp3")