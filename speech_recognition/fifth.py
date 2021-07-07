#Speech recognition means that when humans are speaking, a machine understands it. 
# Here we are using Google Speech API in Python to make it happen. We need to install 
# the following packages for this −

#Pyaudio − It can be installed by using pip install Pyaudio command.

#SpeechRecognition − This package can be installed by using pip install SpeechRecognition.

#Google-Speech-API − It can be installed by using the command pip install google-api-python-client.

import speech_recognition as sr

recording = sr.Recognizer()

with sr.Microphone() as source: 
    recording.adjust_for_ambient_noise(source)
    print("Please Say something:")
    audio = recording.listen(source)

try:
   print("You said: \n" + recording.recognize_google(audio))
except Exception as e:
   print(e)

