import mmap
import os
import time
import sys

# This is the name of the file that we will be reading.
filename = "test.txt"

# Open the file in read-only mode.
file = open(filename, "r+")

# Map the file as read-only.
map = mmap.mmap(file.fileno(), 0, prot=mmap.PROT_READ)

# Read the contents of the file.
print("File before update:")
while True:
    s = map.readline()
    if not s:
        break
    print(s)

# Move the pointer to the beginning of the file.
map.seek(0)

# Write new data to the file.
map.write("Hello, world!\n".encode('utf-8'))

# Close the mmap.
map.close()

# Close the file.
file.close()

# Open the file again, in read-only mode.
file = open(filename, "r+")

# Map the file as read-only.
map = mmap
