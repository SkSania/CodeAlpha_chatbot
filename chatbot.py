def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "thank you ":
        return " You're most welcome"
    elif user_input == "I am sad ":
        return " But y? How can I help you"
    elif user_input == " Okay bye":
        return "Goodbye!"
    else:
        return "I don't understand."


def chat():
    print("🤖 Chatbot: Hello! Type something to begin. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print(f"Bot: {response}")
        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    chat()
