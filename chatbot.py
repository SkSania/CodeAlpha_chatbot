import datetime

def greet_user():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning! ☀️"
    elif 12 <= current_hour < 18:
        return "Good afternoon! 🌤️"
    else:
        return "Good evening! 🌙"

def chatbot():
    print("ChatBot: Hello! I'm your virtual assistant.")
    print(f"ChatBot: {greet_user()}")
    print("ChatBot: Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("ChatBot: Hey there! How can I help you?")
        elif user_input == "how are you":
            print("ChatBot: I'm great, thanks! Hope you're doing well too.")
        elif user_input == "what is your name":
            print("ChatBot: I'm ChatBot 1.0, your Python-coded buddy.")
        elif user_input == "who created you":
            print("ChatBot: A brilliant intern working on Python tasks created me! 😄")
        elif user_input == "what can you do":
            print("ChatBot: I can chat, tell jokes, and help with simple tasks.")
        elif user_input == "tell me a joke":
            print("ChatBot: Why did the computer show up late to work? It had a hard drive! 😂")
        elif user_input in ["thanks", "thank you"]:
            print("ChatBot: Always happy to help! 😊")
        elif user_input in ["what's the time", "tell me the time", "time"]:
            now = datetime.datetime.now().strftime("%I:%M %p")
            print(f"ChatBot: The current time is {now}.")
        elif user_input == "bye":
            print("ChatBot: Bye! Take care and see you soon. 👋")
            break
        else:
            print("ChatBot: Hmm, I didn't get that. Can you say it another way?")

# Run the chatbot
chatbot()
