#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = """Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars"""
# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):# loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
print(text)