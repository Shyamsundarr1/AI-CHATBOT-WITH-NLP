import nltk
from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you",]
    ],
    [
        r"how are you?",
        ["I am doing good, How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!",]
    ],
]

# Define a function to start the chatbot
def chatbot():
    print("Hi, I am your chatbot! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Main execution
if __name__ == "__main__":
    chatbot()
