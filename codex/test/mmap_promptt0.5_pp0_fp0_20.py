import mmap
# Test mmap.mmap(0, 0, "sharedmem", mmap.MAP_SHARED, fd, 0)
# This is a simple example of how to use mmap module
# It simply writes a string to a file and then maps the file in memory
# and prints the contents of the file that is in memory

# Create a file and write a string to it
f = open("test_file", "w+")
f.write("This is a test string")
f.close()

# Open the file again, this time to read and write to the file
# using mmap
f = open("test_file", "r+")
# Map the file into memory
m = mmap.mmap(f.fileno(), 0)
# Read the content via standard file methods
print(m.readline())
# Close the map
m.close()

# Open the file again, this time to read and write to the file
# using mmap
f = open("test_file", "r+")
# Map the file into memory
m = mmap.mmap(f.fileno(), 0)
# Read the
