import mmap
# Test mmap.mmap.read_byte()

# Create a text file
file = open('test.txt', 'w+')
file.write('abcd\n')
file.close()

# Open the file with mmap
file = open('test.txt', 'r+')
m = mmap.mmap(file.fileno(), 0)

# Read the first byte
print(m.read_byte())

# Close the file
m.close()
file.close()

# Delete the file
import os
os.remove('test.txt')
