import mmap
# Test mmap.mmap

# Create a file and write some data to it
with open("test.txt", "w+") as f:
    f.write("Hello World!")

# Open the file
f = open("test.txt", "r+")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())  # prints "Hello World!"

# Update content using slice notation;
# note that new content must have same size
m[6:] = " world!\n"

# ... and read again using standard file methods
m.seek(0)
print(m.readline())  # prints "Hello  world!"

# close the map
m.close()

# close the file
f.close()

# Test mmap.mmap

# Create a file and write some data to it
with open("test.txt", "w+") as f:
    f.write("Hello World!")

# Open the file
f =
