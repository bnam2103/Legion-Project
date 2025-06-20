import pyttsx3

def speak_text(text: str):
    """Speak the given text using the system's TTS engine."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

