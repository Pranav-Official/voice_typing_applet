import speech_recognition as sr
import pyautogui as auto

r = sr.Recognizer()

#AUDIO_FILE = "/home/pranavpp/Projects/Untitled Folder/2020-11-06-10:44:17.wav"

#with sr.AudioFile(AUDIO_FILE) as source:
#    audio = r.record(source)  # read the entire audio file


r = sr.Recognizer()
print("1")
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

print("2")
try:
    txt = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + txt)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

print("3")

auto.typewrite(" ")
auto.typewrite(txt)