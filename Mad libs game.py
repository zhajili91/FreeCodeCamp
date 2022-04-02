"""
https://www.freecodecamp.org/news/python-projects-junior-developers/

Mad libs game
Ask the user for an input.

This could be anything such as a name, an adjective, a pronoun or even an action. Once you get the input,
you can rearrange it to build up your own story.

Here's a youtube tutorial on mad libs in Python.
And example code on Github.

"""

what_is_in_your_mind_input = input("what's on your mind today? \n")
check_count = len(what_is_in_your_mind_input.split(" "))

print("oh nice, you just told me what's on your mind in {} words!".format(check_count))
