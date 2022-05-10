import mmap
# Test mmap.mmap()

# This test is a little different from the others, as it
# doesn't use the `TestCase` class.

# Create a file to mmap
f = open('temp', 'w+')

# Write a line to the file
f.write('This is a test\n')

# Close the file
f.close()

# Open the file for reading
f = open('temp', 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read the content via standard file methods
