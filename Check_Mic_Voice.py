import pyttsx3 as tts
import speech_recognition as sr
from Custom_Speech_Recog_Functions import Setup

speaker = tts.init("sapi5")
voices = speaker.getProperty("voices")

def check_mic_voice():
    print("\n--------------------------Devices-----------------------------\n")
    for mic_idx, mic_name in enumerate(sr.Microphone.list_microphone_names()):
        print(f'Index: {mic_idx} Name: {mic_name} {" ":25}')

    print("\n--------------------------Voices-----------------------------\n")
    # List out available voices
    for voice in voices:
        print(voice)    