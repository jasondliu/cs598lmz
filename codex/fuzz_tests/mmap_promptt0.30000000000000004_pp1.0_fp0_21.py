import mmap
# Test mmap.mmap()

# Create a file
with open("test.txt", "w+") as f:
    f.write("Hello, world!")

# Open the file
f = open("test.txt", "r+")

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print(m.readline())

# Update the memory-map with new data
m.seek(0)
m.write(b"Hello, Python!")

# Close the memory-map
m.close()

# Close the file
f.close()

# Open the file
f = open("test.txt", "r")

# Read the entire file
print(f.read())

# Close the file
f.close()

# Delete the file
os.remove("test.txt")

# Test mmap.mmap()

# Create a file
with open("test.txt", "w+") as f:
    f.write("Hello, world!")

# Open the
