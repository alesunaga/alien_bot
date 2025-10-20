Alien Bot

A simple, rule-based chatbot written in Python. This bot, named Etcetera, is an alien learning about Earth through a command-line conversation. This project was created as part of a Codecademy course.

Features

    Greets the user and asks for their name.
    
    Engages in conversation by asking random questions.
    
    Responds to specific questions based on regular expression matching.
    
    Can perform a simple calculation (cubing a number).
    
    Provides a variety of responses when it doesn't understand the user's input.
    
    Can be exited using common farewell commands (e.g., "bye", "quit", "exit").

How to Run

    Ensure you have Python 3 installed on your system.
    
    Save the code as alien_bot.py.
    
    Open a terminal or command prompt.
    
    Navigate to the directory where you saved the file.
    
    Run the script using the following command:
    
    python alien_bot.py


    Follow the prompts in the terminal to interact with the bot.

How It Works

    The bot uses a dictionary called alienbabble to map "intents" to specific regular expression patterns. When a user provides input, the bot's .match_reply() method iterates through these patterns. If a user's reply matches a pattern, the bot triggers the corresponding method to generate and return an appropriate response. If no patterns are matched, it gives a generic reply from .no_match_intent().

How to Customize

You can easily extend the bot's capabilities by adding new intents and responses.

Add a new intent and regex pattern:
Open alien_bot.py and add a new key-value pair to the self.alienbabble dictionary inside the __init__ method. The key should be a descriptive name for the intent, and the value should be the regular expression to match.

self.alienbabble = {
    'describe_planet_intent': r'.*your planet.*',
    'answer_why_intent': r'why are you (.*)',
    'cubed_intent': r'.*cube.*(\d+)',
    'new_intent_name': r'your new regex pattern' # Add your new intent here
}


Create a new response method:
Write a new method inside the AlienBot class that returns the string or a random choice from a tuple of strings you want the bot to say.

def new_intent_name(self):
  responses = ("This is the first response.", "This is the second response.")
  return random.choice(responses)


Link the intent to the method:
In the .match_reply() method, add a new elif block to connect the new intent to its response method.

# ... inside .match_reply()
elif found_match and intent == 'cubed_intent':
  return self.cubed_intent(found_match.groups()[0])
elif found_match and intent == 'new_intent_name': # Add this block
  return self.new_intent_name()
