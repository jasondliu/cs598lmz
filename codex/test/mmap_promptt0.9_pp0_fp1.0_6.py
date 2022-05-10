import mmap
# Test mmap.mmap instance creation
file = open("test.txt", "r+")
# Create an anonymous memory map
m = mmap.mmap(file.fileno(), 0)
# Write the text to the memory map
m[0:] = "Hello Python world"
m.flush()  # Push data to file
