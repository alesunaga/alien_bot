# importing regex and random libraries
import re
import random

class AlienBot:
  """
  A simple, rule-based chatbot that simulates a conversation with an alien.
  """
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry", "never", 'not today', "no way", "absolutely not", "not interested", "maybe later")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "see you", "farewell", "stop", "end", "adios", "ciao", "disconnect")
  # random starter questions
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? ",
        "What is your favorite season? ",
        "Do you enjoy music? ",
        "What is something interesting about your planet? "
    )

  def __init__(self):
    """
    Initializes the bot with a dictionary of intents and their corresponding regex patterns.
    """
    self.alienbabble = {
        'describe_planet_intent': r'(can you tell me about|i am interested in) your planet', 
        'answer_why_intent': r'why are you (.*)', 
        'cubed_intent': r'.*cube.*(\d+)'
        }

  def greet(self):
    """
    Greets the user and starts the conversation.
    """
    self.name = input("Greetings human, what is your name? ")
    will_help = input(f"Hi {self.name}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? ")
    if will_help in self.negative_responses:
      print("Ok, have a nice Earth day!")
      return
    self.chat()

  def make_exit(self, reply):
    """
    Checks if the user's reply contains any exit commands.
    """
    for word in self.exit_commands:
      if word in reply:
        print("Ok, have a nice Earth day!")
        return True
    return False

  def chat(self):
    """
    Main chat loop that continues until an exit command is given.
    """
    reply = input(random.choice(self.random_questions)).lower()
    while not self.make_exit(reply):
      reply_to_print = self.match_reply(reply)
      print(reply_to_print)
      reply = input(random.choice(self.random_questions)).lower()

  def match_reply(self, reply):
    """
    Matches the user's reply to an intent and returns the appropriate response.
    """
    for intent, regex_pattern in self.alienbabble.items():
      found_match = re.match(regex_pattern, reply)
      if found_match:
        if intent == 'describe_planet_intent':
          return self.describe_planet_intent()
        elif intent == 'answer_why_intent':
          return self.answer_why_intent()
        elif intent == 'cubed_intent':
          return self.cubed_intent(found_match.groups()[0])
        
    # If no match is found after checking all intents, return a generic response.
    return self.no_match_intent()

  def describe_planet_intent(self):
    """
    Returns a response about the alien's home planet.
    """
    responses = ("My planet is a utopia of diverse organisms and species. ", "I am from Opidipus, the capital of the Wayward Galaxies. ")
    return random.choice(responses)

  def answer_why_intent(self):
    """
    Returns a response explaining why the alien is here.
    """
    responses = ("I come in peace.", "I am here to collect data on your planet and its inhabitants.", "I heard the coffee is good." )
    return random.choice(responses)
      
  def cubed_intent(self, number):
    """
    Takes a number as a string, cubes it, and returns the result in a sentence.
    """
    number = int(number)
    cubed_number = number ** 3
    return f"The cube of {number} is {cubed_number}. Isn't that cool? "

  def no_match_intent(self):
    """
    Returns a generic response when the bot doesn't understand.
    """
    responses = ("Please tell me more. ", "Tell me more! ", "Why do you say that? ", "I see. Can you elaborate? ", "Interesting. Can you tell me more? ", "I see. How do you think? ", "Why? ", "How do you think I feel when you say that? ")
    return random.choice(responses)

# Create an instance of AlienBot and start the conversation.
my_bot = AlienBot()
my_bot.greet()

