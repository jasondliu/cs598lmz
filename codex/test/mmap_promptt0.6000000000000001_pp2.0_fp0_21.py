import mmap
# Test mmap.mmap()
# https://docs.python.org/2/library/mmap.html

# Create file
f = open("test.txt", "w+")

# Write to file
f.write("abcde"*10)

# Close file
f.close()

# Open file
f = open("test.txt", "r+")

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using slice assignment
# Note that new content must have same size
m[6:11] = "12345"
m.seek(0)
print(m.readline())

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()
# https://docs.python.org/2/library/mmap.html

# Create file
f = open("test.txt", "w+")

# Write to file
