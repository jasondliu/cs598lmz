import mmap
# Test mmap.mmap()

# Create a file and write a few bytes to it
with open('hello.txt', 'w') as f:
    f.write('hello world')

# Create an mmap object
m = mmap.mmap(f.fileno(), 0)

# Read the first 5 bytes
print(m.read(5))

# Read the next 5 bytes
print(m.read(5))

# Reset the pointer to the beginning
m.seek(0)

# Read the first 5 characters
print(m.read(5))

# Close the mmap object
m.close()

# Close the file
f.close()

# The following code reads the entire file into memory
#with open('hello.txt', 'r') as f:
#    print(f.read(11))

# The following code reads the entire file into memory
with open('hello.txt', 'r') as f:
    print(f.read(11))

# Test mmap.mmap()

