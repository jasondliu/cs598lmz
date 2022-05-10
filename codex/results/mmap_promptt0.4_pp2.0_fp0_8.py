import mmap
# Test mmap.mmap()

# Create a file
f = open("foo", "wb")
f.write("Hello world")
f.close()

# Open the file for reading
f = open("foo", "r+")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print m.readline()

# Update the memory-map with new data
m.seek(0)
m.write("Hello world")

# Close the memory-map
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Create a file
f = open("foo", "wb")
f.write("Hello world")
f.close()

# Open the file for reading
f = open("foo", "r+")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read from the memory-map
print m.readline()
