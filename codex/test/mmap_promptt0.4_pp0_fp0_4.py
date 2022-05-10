import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length[, access[, offset]])
# length -- Number of bytes to map.
# access -- mmap.ACCESS_READ or mmap.ACCESS_WRITE or mmap.ACCESS_COPY
# offset -- Where in the file to start the mapping.

# Create a file
f = open("temp.txt", "w+")
f.write("This is a test string\n")
f.close()

# Open the file
f = open("temp.txt", "r+")

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using file's write method.
m.seek(0)
m.write("This is another test string\n")

# Close the map
