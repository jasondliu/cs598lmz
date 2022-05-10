import mmap
# Test mmap.mmap()

# Open file and get size
f = open("test.txt", "r+")
f.write("1234567890" * 100)
f.seek(0)

# Map file
m = mmap.mmap(f.fileno(), 0)

# Read from file
print m[0:10]

# Write to file
m[0:10] = "ABCDEFGHIJ"

# Close file
m.close()
f.close()

# Open file and print contents
f = open("test.txt", "r")
print f.read()
f.close()
# Test mmap.mmap()

# Open file and get size
f = open("test.txt", "r+")
f.write("1234567890" * 100)
f.seek(0)

# Map file
m = mmap.mmap(f.fileno(), 0)

# Read from file
print m[0:10]

# Write to file
m[0:10] = "ABCDEFGHIJ"

# Close file
m
