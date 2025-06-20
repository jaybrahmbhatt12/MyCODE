def chatbot():
    print("Welcome to CodeAlpha Chatbot!")
    print("Type something to start a conversation (type 'exit' to stop)")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Heyy!!!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! What about you?")
        elif user_input == "Good":
            print("Bot: That's Great!!")
        elif user_input == "what is your name":
            print("Bot: I'm your friend chatbot.")
        elif user_input == "help":
            print("Bot: You can say things like 'hello', 'how are you', 'bye'.")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        elif user_input == "exit":
            print("Bot: Chat ended.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
