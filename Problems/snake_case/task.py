# Since we are learning Python, sometimes it might be useful to convert texts from lowerCamelCase to snake_case.
# The main trick is to find the correct place where to insert an underscore.
# Let's make a rule that it's right before a capital letter of the next word.

import string

new_string = []
separator = ""
raw_string = input()
for char in raw_string:
    if char in string.ascii_uppercase:
        new_string.append("_" + char.lower())
    else:
        new_string.append(char)

print(separator.join(new_string))
