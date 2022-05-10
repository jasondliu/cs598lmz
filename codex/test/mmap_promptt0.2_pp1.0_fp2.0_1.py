import mmap
# Test mmap.mmap()

# Create a file
with open("test.txt", "w") as f:
    f.write("Hello, world!")

# Open the file
f = open("test.txt", "r+")

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from the mmap object
print(m.readline())

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Create a file
with open("test.txt", "w") as f:
    f.write("Hello, world!")

# Open the file
f = open("test.txt", "r+")

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from the mmap object
print(m.readline())

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Create
