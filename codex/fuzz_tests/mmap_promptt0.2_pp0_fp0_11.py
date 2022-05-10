import mmap
# Test mmap.mmap()

# Open file
f = open("test.txt", "r+")

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print file contents
print m[:]

# Close map and file
m.close()
f.close()

# Test mmap.mmap()

# Open file
f = open("test.txt", "r+")

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Read from memory
print m.readline()

# Close map and file
m.close()
f.close()

# Test mmap.mmap()

# Open file
f = open("test.txt", "r+")

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Write to memory
m.write("Hello Python!")

# Close map and file
m.close()
f.close()

# Test mmap.mmap()

# Open file
f = open("test.txt",
