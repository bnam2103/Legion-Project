from openai import OpenAI

def chat_with_bot(user_text: str) -> str:

    if not hasattr(chat_with_bot, "client"):
        chat_with_bot.client = OpenAI(api_key="12345")  # Replace with your actual key
        chat_with_bot.chat_history = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]

    chat_with_bot.chat_history.append({"role": "user", "content": user_text})

    try:
        response = chat_with_bot.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_with_bot.chat_history
        )

        reply = response.choices[0].message.content.strip()
        chat_with_bot.chat_history.append({"role": "assistant", "content": reply})
        return reply

    except Exception as e:
        return f"[Error] {e}"

# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["exit", "quit"]:
#         print("Goodbye!")
#         break
#     bot_response = chat_with_bot(user_input)
#     print("Bot:", bot_response)

