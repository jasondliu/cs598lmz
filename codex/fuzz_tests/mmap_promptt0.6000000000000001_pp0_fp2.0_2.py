import mmap
# Test mmap.mmap()
#
# https://docs.python.org/3/library/mmap.html

# Create a file
f = open('test.txt', 'wb')
f.write(b'0123456789abcdef')
f.close()

# Open for reading and writing
f = open('test.txt', 'r+b')

# Create mmap
m = mmap.mmap(f.fileno(), 0)

# Read and write to the mmap
m[0:3]
m[9:12]
m.seek(0)
m.write(b'ABC')
m.seek(9)
m.write(b'XYZ')
m.close()

# Close the file, and open it again
f.close()
f = open('test.txt', 'rb')
f.read()
f.close()
