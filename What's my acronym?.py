"""
Ask the user to enter the full meaning of an organization or concept, and you'll provide the acronym to the user.
For example:
Input -> As Soon As Possible. Output -> ASAP.
Input -> World Health Organization. Output -> WHO.
Input -> Absent Without Leave. Output -> AWOL.
"""
#fixing the bug for different letter issue

acronym = ""
input_the_sentence = input("Please enter a sentence to generate Acronym: ")
words = input_the_sentence.replace('Of', '').split()  # replace "Of" with space and then split list with space char
print(words)

for i in words:
    acronym = i [ 0 ].upper() + acronym
print("Acronym is ==> ", acronym [ ::-1 ])  # reverse string with slicing
