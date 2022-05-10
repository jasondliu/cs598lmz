import mmap
# Test mmap.mmap

# Open file
f = open("/tmp/test.txt", "w+")

# Write to file
f.write("Hello World")
f.write("This is our new text file")
f.write("and this is another line.")
f.write("Why? Because we can.")

# Close file
f.close()

# Open file
f = open("/tmp/test.txt", "r+")

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
print(m.readline())

# Read content via slice notation
print(m[:5])  # prints "Hello"

# Update content using slice notation;
# note that new content must have same size
m[6:] = " world!\n"

# ... and read again using standard file methods
m.seek(0)
print(m.readline())

# close the map
m.close()

# close the file
f.close()

# Test mmap.
