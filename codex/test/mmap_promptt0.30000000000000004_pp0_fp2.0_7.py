import mmap
# Test mmap.mmap

# Create a new file
f = open("test.txt", "w+")

# Write to the file
f.write("Hello World")

# Close the file
f.close()

# Open the file again
f = open("test.txt", "r+")

# Map the file into memory
m = mmap.mmap(f.fileno(), 0)

# Read from the file
print(m.readline())

# Close the file
f.close()

# Delete the file
import os
os.remove("test.txt")
 

# Test mmap.mmap with offset

# Create a new file
f = open("test.txt", "w+")

# Write to the file
f.write("Hello World")

# Close the file
f.close()

# Open the file again
f = open("test.txt", "r+")

# Map the file into memory
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

# Write to the file
