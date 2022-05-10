import mmap
# Test mmap.mmap.read_byte()
# https://docs.python.org/2/library/mmap.html

# Create a file
f = open('test.txt', 'wb')
f.write('Hello Python!')
f.close()

# Open a file
f = open('test.txt', 'r+')

# Map file to memory
m = mmap.mmap(f.fileno(), 0)

# Print the entire file
print m.read(11)

# Print the first byte
print m.read_byte()

# Print the next byte
print m.read_byte()

# Print the next 4 bytes as an integer
print m.read_byte(4)

# Close the map
m.close()

# Close the file
f.close()

# Delete the file
import os
os.remove('test.txt')

# Create a file
f = open('test.txt', 'wb')
f.write('Hello Python!')
f.close()

# Open a file
f = open('test.txt', 'r+')

