import mmap
# Test mmap.mmap parameters
f = open('test.txt', 'w+b')
m = mmap.mmap(f.fileno(), 0)
#print(m)
print(repr(m))
# Map length is zero
print(len(m))
# Write bytes to file
m.write(b"Hello world!")
# Map length is now non-zero
print(len(m))
#print(m.seek(0))
#print(m.read(len(m)))
m.close()
f.close()

# Using mmap to create memory mapped files
import mmap
# Create a memory mapped file
f = open('test.txt', 'r+b')
m = mmap.mmap(f.fileno(), 0)
# Read the whole file
print('Before: {0}'.format(repr(m[:])))
# Write 'abcdefghijkl'
m[6:] = b'abcdefghijkl'
# Read the whole file
print('After : {0}'.format(repr(m[:])))
# Close the memory mapped file

