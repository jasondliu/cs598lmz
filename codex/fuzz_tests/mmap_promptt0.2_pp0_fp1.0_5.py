import mmap
# Test mmap.mmap()

# Open file
f = open("test.txt", "r+")

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print file contents
print m.readline()

# Update content and save
m.seek(0)
m.write("Hello Python!\n")
m.write("Hello World!\n")
m.close()

# Close file
f.close()

# Open file
f = open("test.txt", "r+")

# Print file contents
print f.readline()

# Close file
f.close()

# Test mmap.mmap()

# Open file
f = open("test.txt", "r+")

# Create memory map
m = mmap.mmap(f.fileno(), 0)

# Print file contents
print m.readline()

# Update content and save
m.seek(0)
m.write("Hello Python!\n")
m.write("Hello World!\n")
m.close()

# Close file
