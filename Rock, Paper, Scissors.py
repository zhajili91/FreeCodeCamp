"""
This is a popular game played between two people. Each player gets to form one of three shapes using their hand:

rock (a closed fist)
paper (a flat hand)
scissors (a fist with the index finger and middle finger extended, forming a V)

"""

# https://realpython.com/python-rock-paper-scissors/

import random  # will be used to input computer choice randomly

user_action = input("Enter a choice (rock, paper, scissors): ")  # our choice
possible_actions = [ "rock", "paper", "scissors" ]  # all possible choices to be used for computer
computer_action = random.choice(possible_actions)  # creating computer action with random module ,possible actions
# list will be used as argument

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
