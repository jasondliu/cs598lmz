import mmap
# Test mmap.mmap
# https://docs.python.org/3/library/mmap.html

# Create a file and write some data
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

# Open the file
f = open("hello.txt", "r+b")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())  # prints b"Hello Python!\n"

# Update content using slice notation;
# note that new content must have same size
m[6:12] = b" world"

# ... and read again using standard file methods
m.seek(0)
print(m.readline())  # prints b"Hello  world!\n"

# close the map
m.close()

# close the file
f.close()

# Test mmap.ACCESS_COPY
# https://docs.python.org/3/library/
