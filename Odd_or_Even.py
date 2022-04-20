"""
https://www.freecodecamp.org/news/python-projects-junior-developers/
"""

while True:
    input_number = int(input("What number are you thinking?: \n"))
    if input_number % 2 == 0:
        print("That's even number! Have another?  ")
    else:
        print("That's and odd number! Have another? ")