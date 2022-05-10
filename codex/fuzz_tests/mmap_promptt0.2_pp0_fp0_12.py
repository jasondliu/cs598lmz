import mmap
# Test mmap.mmap.readline()

# Create a file with some data
with open("test.txt", "w") as f:
    f.write("Hello world\n")
    f.write("This is a test\n")
    f.write("This is only a test\n")

# Open the file
f = open("test.txt", "r")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read the first line
print(m.readline())

# Read the next line
print(m.readline())

# Read the rest of the file
print(m.read())

# Close the map
m.close()

# Close the file
f.close()

# Test mmap.mmap.find()

# Create a file with some data
with open("test.txt", "w") as f:
    f.write("Hello world\n")
    f.write("This is a test\n")
   
