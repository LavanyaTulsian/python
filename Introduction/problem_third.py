# Code taken from chatgpt
# / represents the current main directory (here it represents the C drive)

import os

# Specify the directory path
path = '/'  # Replace with your desired path

# Get the list of all files and directories
content = os.listdir(path)

# give a list of all the contents
print(content)

# prints each content from the content list as a single item in a new line and not as a list
print(f"Contents of '{path}':")
for item in content:
    print(item)
