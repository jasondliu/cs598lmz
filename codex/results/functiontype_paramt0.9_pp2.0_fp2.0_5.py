from types import FunctionType
list(FunctionType(c.globals["b"], globals(), "a")() for a in range(10))

# Step 10:
# Import time module
import time

# Return the number of milliseconds since the epoch
print(time.time())

# Step 14:
# Reads the entire contents of a file into a string
with open('C:/Users/Hanna/Desktop/file1.txt', 'r') as file_to_read:
    contents = file_to_read.read()
    print(contents)

# Step 16
# Check if a file exists
import os

if os.path.exists('C:/Users/Hanna/Desktop/file1.txt'):
    print('Yes')
else:
    print('No')

# Step18:
# Appends half of the content of the file to the other half
with open('C:/Users/Hanna/Desktop/file1.txt', 'r') as filetoread:
    contents = filetoread.read()
with open('C:/Users/Hanna/Desktop/file1.txt', 'w')
