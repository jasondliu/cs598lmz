import mmap
# Test mmap.mmap()

# test_mmap.py
import os
import mmap

# Create a file and memory-map it
f = open('hello.txt', 'w')
f.write('Hello Python!')
f.close()

f = open('hello.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Read from memory
print(m.readline())

# Update the file from memory
m.seek(0)
m.write(b'Hello World!')

# Close the memory map
m.close()

# Close the underlying file
f.close()

# Delete the file
os.remove('hello.txt')

# Test mmap.mmap()

# test_mmap.py
import os
import mmap

# Create a file and memory-map it
f = open('hello.txt', 'w')
f.write('Hello Python!')
f.close()

f = open('hello.txt', 'r+')
m = mmap.mmap(f.fileno(), 0
