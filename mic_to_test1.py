import speech_recognition as sr

recognizer = sr.Recognizer()

def mic1():
    with sr.Microphone(device_index=1) as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")

        audio = recognizer.listen(source)
        print("Recognizing....")

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            return None
        except sr.RequestError as e:
            print("Error occurred; {0}".format(e))
            return text
if __name__=="__main__":
    mic1()
