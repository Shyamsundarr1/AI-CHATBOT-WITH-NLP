# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLOUTIONS

*NAME*: KEESARI SHYAMSUNDAR REDDY

*INTERN ID*: CT6WNYN

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

*PLATFORM USED*: VISUAL STUDIO CODE

*DESCRIPTION*:

This program leverages the nltk library to create a simple rule-based chatbot. The chatbot engages in conversations with users by matching their input with predefined patterns and responding with corresponding replies. It’s a fundamental example of how chatbots function using pattern matching and predefined responses.

Components
NLTK Library:

The nltk (Natural Language Toolkit) library is a powerful suite of libraries and programs for symbolic and statistical natural language processing in Python. The nltk.chat.util module provides utility functions to create chatbots.

Patterns and Responses:

The heart of this chatbot is a list of patterns and their corresponding responses. Patterns are defined using regular expressions, which enable matching against user input. Each pattern has an associated response or set of responses.

Key Sections
Patterns and Responses
The pairs list consists of tuples where each tuple represents a pattern and its corresponding responses. Regular expressions in the patterns help to identify user input and match it to an appropriate response. The chatbot’s responses are predefined, making it rule-based.

For example, the pattern r"my name is (.*)" captures the user’s name using a regular expression group (.*). The corresponding response "Hello %1, How can I help you today?" uses %1 to refer to the captured name from the user’s input. This dynamic aspect allows the chatbot to interact more naturally.

Other patterns include simple greetings like hi, hey, and hello which have standard responses such as "Hello" and "Hey there". There are also patterns for common questions like what is your name?, and conversational phrases like how are you? with appropriate responses to keep the conversation flowing.

Chat Initialization
The Chat class from nltk.chat.util is utilized to create a chatbot instance. This class takes the pairs list and reflections dictionary as arguments. The reflections dictionary maps pronouns and other words to their conversational counterparts, helping the chatbot handle some variations in user input.

For instance, if the user says “I am fine,” the chatbot can recognize “I” and reflect it as “you” in responses like “Great to hear that, how can I help you?”

Chatbot Function
The chatbot function is defined to initialize the chatbot and start the conversation. When the function is called, it prints a greeting message and instructs the user to type 'quit' to exit the chat. The converse method of the Chat class is then called, initiating an interactive session where the chatbot listens to user input, matches it to patterns, and responds accordingly.

Main Execution
The if __name__ == "__main__": block ensures that the chatbot function is called only when the script is executed directly, not when imported as a module. This structure is typical in Python scripts to prevent code from running unintentionally during imports.

NLTK (Natural Language Toolkit):

This library is essential for the chatbot functionalities and natural language processing tasks. Install it using the following command:
pip install nltk

Summary
The chatbot program exemplifies a straightforward yet effective approach to creating conversational agents using predefined patterns and responses. It showcases the use of regular expressions for pattern matching and the utility of the nltk library for natural language processing tasks. While the chatbot is basic, its structure provides a foundation for more complex interactions and improvements, such as adding more patterns, responses, and integrating machine learning models for enhanced capabilities. The chatbot’s ability to engage users with personalized responses adds a touch of interactivity, making it an excellent starting point for those interested in developing conversational AI.
