import mmap
# Test mmap.mmap()

# Create a file and write some data to it
with open("hello.txt", "wb") as f:
    f.write("Hello Python!\n")

# Open the file
f = open("hello.txt", "r+b")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print m.readline()

# Update the memory-map with new data
m.seek(0)
m.write("Hello World!\n")

# Close the memory-map
m.close()

# Close the file
f.close()

# Open the file
f = open("hello.txt", "r+b")

# Read from the file
print f.readline()

# Close the file
f.close()

# Delete the file
os.remove("hello.txt")

# Test mmap.mmap()

# Create a file and write some data to it
with open("hello.txt", "wb") as
