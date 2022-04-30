"""
This is a popular game played between two people. Each player gets to form one of three shapes using their hand:

rock (a closed fist)
paper (a flat hand)
scissors (a fist with the index finger and middle finger extended, forming a V)

"""

# https://realpython.com/python-rock-paper-scissors/

import random  # will be used to input computer choice randomly

user_action = input("Enter a choice (rock, paper, scissors): ") # our choice
possible_actions = ["rock", "paper", "scissors"]  # all possible choices to be used for computer
computer_action = random.choice(possible_actions) # creating computer action with random module ,possible actions
# list will be used as argument

print("\nYou are choosing {}".format(user_action),"computer is choosing {}\n".format(computer_action))
