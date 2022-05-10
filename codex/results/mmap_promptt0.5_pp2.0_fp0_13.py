import mmap
# Test mmap.mmap()

# Create a file and fill it with some data
filename = "foo"

# Open a file in write-only mode
f = open(filename, "w+b")

# Write some data to the file
f.write(b"Hello Python!\n")

# Close the file
f.close()

# Open the file for reading
f = open(filename, "r+b")

# Create a memory-map to the file
m = mmap.mmap(f.fileno(), 0)

# Read the content via standard file methods
print(m.readline())

# Update the file content
m[6:] = b" world!\n"

# Read the file again
m.seek(0)
print(m.readline())

# Close the map
m.close()

# Close the file
f.close()

# Open the file for writing
f = open(filename, "w")

# Write the new contents to disk
f.write("Hello Python!\n")
f.write("Hello World!\n")


