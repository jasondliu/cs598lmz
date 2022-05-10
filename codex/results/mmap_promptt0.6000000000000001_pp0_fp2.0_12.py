import mmap
# Test mmap.mmap()

# Read a file into memory
f = open("test.txt", 'r+b')
m = mmap.mmap(f.fileno(), 0)

# Print the entire file
print m[:]

f.close()
m.close()

# Test mmap.mmap()

# Read a file into memory
f = open("test.txt", 'r+b')
m = mmap.mmap(f.fileno(), 0)

# Print the entire file
print m[:]

# Change a single character
m[0] = 'x'

f.close()
m.close()

# Test mmap.mmap()

# Read a file into memory
f = open("test.txt", 'r+b')
m = mmap.mmap(f.fileno(), 0)

# Print the entire file
print m[:]

# Change a single character
m[0] = 'x'

# Save the changes
m.flush()

f.close()
m.close()

# Test mmap.mm
