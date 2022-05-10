import mmap
# Test mmap.mmap()
# https://docs.python.org/3.6/library/mmap.html

# Create a file
f = open("hello.txt", "w+")
f.write("Hello Python!\n")
f.close()

# Open the file
f = open("hello.txt", "r+")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Update content using slice notation;
# note that new content must have same size
m[6:13] = b"world"
m.seek(0)
print(m.readline())

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()
# https://docs.python.org/3.6/library/mmap.html

# Create a file
f = open("hello.txt", "w+")
f.write("Hello Python!\n")
f
