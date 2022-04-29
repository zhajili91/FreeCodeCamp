"""
Ask the user to enter the full meaning of an organization or concept, and you'll provide the acronym to the user.
For example:
Input -> As Soon As Possible. Output -> ASAP.
Input -> World Health Organization. Output -> WHO.
Input -> Absent Without Leave. Output -> AWOL.
"""
# following code could be written in better way ,no time :)

acronym = ""
input_the_sentence = input("Please enter a sentence to generate Acronym: ")
words = input_the_sentence.replace('Of', '').split()  # replace "Of" with space and then split list with space char

if "of" in words:
    words.remove("of")

for i in words:
    acronym = i [ 0 ].upper() + acronym
print("Acronym is ==> ", acronym [ ::-1 ])  # reverse string with slicing
