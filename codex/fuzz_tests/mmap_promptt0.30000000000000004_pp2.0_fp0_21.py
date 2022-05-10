import mmap
# Test mmap.mmap()

# Create a file
f = open("test.txt", "w+")
f.write("Hello World")
f.close()

# Open the file
f = open("test.txt", "r+")

# Create a memory map
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print("Before:", m.readline())

# Re-position to the beginning of the file
m.seek(0)

# Overwrite the file with new content
m.write("Hello Python!")

# Re-position to the beginning of the file
m.seek(0)

# Read content via standard file methods
print("After:", m.readline())

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Create a file
f = open("test.txt", "w+")
f.write("Hello World")
f.close()

# Open the file
f = open("test.txt", "r+")
