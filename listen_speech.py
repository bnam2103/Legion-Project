import speech_recognition as sr

def listen_to_speech(prompt: str = "Say something...") -> str:
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    recognizer.pause_threshold = 1.5
    print(prompt)

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""

    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
        return ""
    
# if __name__ == "__main__":
#     listen_to_speech()