import mmap
# Test mmap.mmap()
# Create an mmap'ed file object
f = open('test.dat', 'r+')
mf = mmap.mmap(f.fileno(), 0)
# Write a few bytes to the start of the buffer
mf.write('abcd')
# Move to the start of the buffer
mf.seek(0)
# Read a few bytes
