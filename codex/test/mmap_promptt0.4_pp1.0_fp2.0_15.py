import mmap
# Test mmap.mmap

# Open a file
f = open("test.txt", "w+")

# Write to file
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))

# Close the file
f.close()

# Open the file
f = open("test.txt", "r+")

# Create a memory-map to the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())  # prints "This is line 1"

# Update content using slice notation;
# note that new content must have same size
m[6:11] = "a"  # now content is "This a line 1"

# ... and read again using standard file methods
m.seek(0)  # rewind
print(m.readline())  # prints "This a line 1"

# close the map
