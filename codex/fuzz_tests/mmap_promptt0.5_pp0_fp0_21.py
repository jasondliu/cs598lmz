import mmap
# Test mmap.mmap

# Create a file
with open('test.txt', 'w+b') as f:
    pass

# Open the file
f = open('test.txt', 'r+b')

# Create a memory-map object
m = mmap.mmap(f.fileno(), 0)

# Print the object
print(m)

# Close the file
f.close()

# Create a file
with open('test2.txt', 'w+b') as f:
    pass

# Open the file
f = open('test2.txt', 'r+b')

# Create a memory-map object
m = mmap.mmap(f.fileno(), 0)

# Print the object
print(m)

# Close the file
f.close()

# Create a file
with open('test3.txt', 'w+b') as f:
    pass

# Open the file
f = open('test3.txt', 'r+b')

# Create a memory-map object
m = mmap.mmap(f.fileno
