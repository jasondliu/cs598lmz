import mmap
# Test mmap.mmap

# mmap.mmap is a memory map of a file. It is used to access the contents of the file in an efficient manner.
# It is also used for shared memory between processes.
# https://www.geeksforgeeks.org/python-mmap-module/

# Create a memory map to a file
m = mmap.mmap(0, 1024, "test.txt")

# Read from a memory map
print(m[0:10])

# Write to a memory map
m[0:10] = "My name is"

# Close the memory map
m.close()

# Open the file in read mode
f = open("test.txt", "r")

# Read the contents of the file
print(f.read())

# Close the file
f.close()

# Remove the file
os.remove("test.txt")

#mmap.mmap()
# mmap.mmap(fileno, length, tagname=None, access=mmap.ACCESS_DEFAULT, offset=0)
# fileno is the file descriptor.
