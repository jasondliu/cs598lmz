import mmap
# Test mmap.mmap.read_byte()

# Create a file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

# Open the file
with open("hello.txt", "r+b") as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read an ASCII line
    print(mm.readline())  # prints "Hello Python!"
    # Read the rest of the file
    print(mm.read())  # prints "Hello Python!"
    # Close the map
    mm.close()

# Test mmap.mmap.read()

# Create a file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

# Open the file
with open("hello.txt", "r+b") as f:
    # Memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # Read an
