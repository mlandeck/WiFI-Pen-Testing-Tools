# usage: python WPAChomper.py
# you must have the wordlist you are trying to transform in the same directory as WPAChomper.py
# the wordlist MUST be named "wordlist.txt"
# WPA pre-shared keys (aka passwords) must be at least 8 characters in length, and have no unprintable ascii characters
# this script will take an existing password list such as rockyou.txt and remove any entries that cannot be use for WPA passwords

import string

with open("wordlist.txt", "r") as f:
    words = f.readlines()

# Remove newline characters from the list of words
words = [word.strip() for word in words]

# Define a list to store the valid words
valid_words = []

# Iterate through the list of words
for word in words:
    # Check if the word is at least 8 characters long
    if len(word) >= 8:
        # Check if the word contains only printable ASCII characters
        if all(c in string.printable for c in word):
            valid_words.append(word)

# Write the valid words to a new file
with open("WPAwordlist.txt", "w") as f:
    for word in valid_words:
        f.write(word + "\n")

