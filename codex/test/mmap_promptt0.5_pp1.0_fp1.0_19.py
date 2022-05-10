import mmap
# Test mmap.mmap()

# Create file
with open("hello.txt", "wb") as f:
    f.write("Hello Python!\n".encode())

# Memory-map the file, size 0 means whole file
f = open("hello.txt", "r+b")
m = mmap.mmap(f.fileno(), 0)
# Read content via standard file methods
print(m.readline())  # prints "Hello Python!"
# Read content via slice notation
print(m[:5])  # prints "Hello"
# Update content using slice notation;
# note that new content must have same size
m[6:] = " world!\n".encode()
# ... and read again using standard file methods
m.seek(0)
print(m.readline())  # prints "Hello  world!"
# close the map
m.close()

# close the file
f.close()

# Test mmap.mmap()

# Create file
with open("hello.txt", "wb") as f:
    f.write("Hello Python!\n".encode())

