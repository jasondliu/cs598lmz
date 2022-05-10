import mmap
# Test mmap.mmap()
# https://docs.python.org/3/library/mmap.html

# Create a file and open it for writing
f = open("test.txt", "w+")

# Write some text to the file
f.write("Hello World")

# Close the file
f.close()

# Open the file again
f = open("test.txt", "r+")

# Create a memory map to the file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory map
print(m.readline())

# Close the memory map
m.close()

# Close the file
f.close()

# Open the file again
f = open("test.txt", "r+")

# Create a memory map to the file
m = mmap.mmap(f.fileno(), 0)

# Write to the memory map
m.write(b"That's all, folks!")

# Close the memory map
m.close()

# Close the file
f.close()

# Open the file again

