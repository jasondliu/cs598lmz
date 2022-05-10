import mmap
# Test mmap.mmap()

# Open a file as a memory-mapped object
f = open("test.txt", "r+")
m = mmap.mmap(f.fileno(), 0)

# Read the first line of the file
print("Before:", m.readline())

# Move to the beginning of the file and write a new line
m.seek(0)
m.write(b"Hello Python!\n")

# Move to the beginning of the file and read the new line
m.seek(0)
print("After:", m.readline())

# Close the memory-mapped object
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Open a file as a memory-mapped object
f = open("test.txt", "r+")
m = mmap.mmap(f.fileno(), 0)

# Read the first line of the file
print("Before:", m.readline())

# Move to the beginning of the file and write a new line
m.seek(0)
m
