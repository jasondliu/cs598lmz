import mmap
# Test mmap.mmap()

# Open the file for reading
f = open('hello.txt', 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from file
print(m.readline())

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open the file for reading
f = open('hello.txt', 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from file
print(m.readline())

# Close the mmap object
m.close()

# Close the file
f.close()
