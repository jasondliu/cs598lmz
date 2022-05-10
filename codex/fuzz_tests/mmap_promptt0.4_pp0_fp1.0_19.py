import mmap
# Test mmap.mmap

# Create a file
f = open("test.txt", "wb")

# Write to the file
f.write("Hello world!")

# Close the file
f.close()

# Open the file
f = open("test.txt", "r+b")

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print m[:]

# Close the memory-map
m.close()

# Close the file
f.close()

# Test mmap.mmap

# Create a file
f = open("test.txt", "wb")

# Write to the file
f.write("Hello world!")

# Close the file
f.close()

# Open the file
f = open("test.txt", "r+b")

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print m[:]

# Close the memory-map
m
