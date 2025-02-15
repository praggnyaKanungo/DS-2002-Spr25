#!/Library/Frameworks/Python.framework/Versions/3.13/bin/python3

import os

favorite_color = input("What is your favorite color? Please enter it here: ")
birth_stone = input("What is your birth stone? Please enter it here:  ")
programming_language = input("What is your favorite programming language? Please enter it here: ")
os.environ["FAVORITE_COLOR"] = favorite_color
os.environ["BIRTH_STONE"] = birth_stone
os.environ["FAVORITE_PROGRAMMING_LANGUAGE"] = programming_language
print("Favorite Color:", os.getenv("FAVORITE_COLOR"))
print("Birth Stone:", os.getenv("BIRTH_STONE"))
print("Favorite Programming Language:", os.getenv("FAVORITE_PROGRAMMING_LANGUAGE"))



