
import speech_recognition as s_r

r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index

with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source)  # reduce noise
    audio = r.listen(source) #take voice input from the microphone
    print(r.recognize_google(audio))
    print("done")

