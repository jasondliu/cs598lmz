import mmap
# Test mmap.mmap()

# Create a file
f = open("data.txt", "w+")

# Write to the file
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))

# Close the file
f.close()

# Open the file
f = open("data.txt", "r+")

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read from the mmap object
print(m.readline())

# Close the mmap object
m.close()

# Close the file
f.close()

# Test mmap.mmap()

# Create a file
f = open("data.txt", "w+")

# Write to the file
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))

# Close the file
f.close()

# Open the file
f = open("data.txt", "r+")

# Create a mmap
