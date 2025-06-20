from listen_speech import listen_to_speech
from ai_voice_1 import speak_text
from chatbot import chat_with_bot
from legion_activation import wait_for_wake_word
from question_or_command import is_question_or_command
from command import AI_command




if __name__ == "__main__":  
    wait_for_wake_word()
    speak_text("Helloooo!")
    while True:
        spoken_input = listen_to_speech("Speak now or say 'quit' to exit:")

        if not spoken_input.strip():
            manual_input = input("Please type your message (or 'quit' to exit): ").strip()
            if manual_input.lower() in ["quit", "exit"]:
                print("Goodbye!")
                speak_text("Goodbye!")
                break
            if manual_input == "": #Go back to the loop for bug fixing
                continue
            user_input = manual_input
        else:
            user_input = spoken_input

        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            speak_text("Goodbye!")
            break
        
        kind = is_question_or_command(user_input)

        if kind == 'question':
            reply = chat_with_bot(user_input)
            print("Bot:", reply)
            speak_text(reply)
        else:
            print(f"Detected question, searching for: {user_input}")
            speak_text(f"Searching for: {user_input}")
            AI_command(user_input)
