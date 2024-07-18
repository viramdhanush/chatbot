import random
import nltk
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Predefined responses
responses = {
    "hi": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm a chatbot, so I'm always good!", "Doing great! How about you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

# Function to get response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I don't understand that."

# Main chatbot loop
def chatbot():
    print("Chatbot: Hi! How can I help you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
