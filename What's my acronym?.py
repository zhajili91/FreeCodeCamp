"""
Ask the user to enter the full meaning of an organization or concept, and you'll provide the acronym to the user.
For example:
Input -> As Soon As Possible. Output -> ASAP.
Input -> World Health Organization. Output -> WHO.
Input -> Absent Without Leave. Output -> AWOL.
"""

acronym = ""
input_the_sentence = input("Please enter a sentence to generate Acronym: ")
words = input_the_sentence.split(" ")
print(words)