import pyttsx3 as tts
import speech_recognition as sr

# Initiate the speaker
speaker = tts.init("sapi5")

voices = speaker.getProperty("voices")

# Initiate the ear
robot_ear = sr.Recognizer()

def set_mic(mic_idx=None, auto_choose_mic = True):
    # Choose mic
    if (auto_choose_mic == False):
        mic = sr.Microphone(mic_idx)  
    else: mic = sr.Microphone()
    return mic

def set_voice(voice_idx=1, voice_speaking_rate=150):
    speaker.setProperty("voice", voices[voice_idx].id)
    speaker.setProperty('rate', voice_speaking_rate)

    rate = speaker.getProperty('rate')

    print(f"Voice: {voices[voice_idx].id}")
    print(f'Speaking rate: {rate}')