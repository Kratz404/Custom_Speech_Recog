import pyttsx3 as tts
import speech_recognition as sr
from Custom_Speech_Recog_Functions import Setup

robot_ear = sr.Recognizer()

def Speech_to_text_EN(mic = Setup.set_mic()):
    with mic as source:
        robot_ear.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = robot_ear.listen(source)
    try:
        text = robot_ear.recognize_google(audio, language='en-EN')
    except:
        text = ""
    return text


def Speech_to_text_VN(mic = Setup.set_mic()):
    with mic as source:
        robot_ear.adjust_for_ambient_noise(source)
        print("Đang nghe...")
        audio = robot_ear.listen(source)
    try:
        text = robot_ear.recognize_google(audio, language='vi-VN')
    except:
        text = ""
    return text