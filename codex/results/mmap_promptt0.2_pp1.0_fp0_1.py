import mmap
# Test mmap.mmap

# Create a file and write some data to it
f = open('test.txt', 'w+')
f.write('Hello World')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map; this will return 'Hello World'
print m[:]

# Close the memory-map
m.close()

# Close the file
f.close()

# Test mmap.mmap

# Create a file and write some data to it
f = open('test.txt', 'w+')
f.write('Hello World')
f.close()

# Open the file
f = open('test.txt', 'r+')

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map; this will return 'Hello World'
print m
