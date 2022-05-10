import mmap
# Test mmap.mmap

# Create a file and write some data to it
with open("hello.txt", "wb") as f:
    f.write("Hello Python!\n")

# Open the file
f = open("hello.txt", "r+b")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

