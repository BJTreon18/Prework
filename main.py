import random

#Simple chat program
#Responds randomly with one of four preprogrammed responses

def generate_response(user_input):
  responses = [
    "We open at 9:45 AM and close at 9 PM on Monday to Sunday.",
    "Our address Kalahari Resorts & Conventions - Round Rock, 3001 Kalahari Blvd, Round Rock, TX 78665",
    "We sell many food items and arcade passes as well as waterpark passes for our guests. ",
    "The prices of our food is rather cheap and water park passes go up to 120 per person. The arcade game cards are as much as you put into the card."
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'

  user_input = input("Hello, how are you?\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()