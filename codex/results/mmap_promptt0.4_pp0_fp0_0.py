import mmap
# Test mmap.mmap()

# Create a memory-map to a file, and close the file
f = open('bigfile', 'w+')
f.write('\x00' * 10000000)
f.close()
m = mmap.mmap(f.fileno(), 10000000)

# Read the content via standard file methods
print m.read(10)
print m.readline()
print m.readline()

# Update content using slice notation;
# note that new content must have same size
m[0:11] = 'Hello World'
m.close()

# Re-open the file and mmap
f = open('bigfile', 'r+')
m = mmap.mmap(f.fileno(), 10000000)

# Verify that changes were made
print m.read(11)

# Close the map and file
m.close()
f.close()

# Test mmap.mmap()

# Create a memory-map to an X-bit file, and close the file
f = open('bigfile', 'w+')
f.write('\x00
