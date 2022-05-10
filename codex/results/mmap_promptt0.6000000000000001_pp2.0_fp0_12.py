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
print 'Read string:', mf.read(4)
# Close the mmap and the underlying file
mf.close()
f.close()

# Test mmap.mmap() with offset and size
# Create an mmap'ed file object
f = open('test.dat', 'r+')
mf = mmap.mmap(f.fileno(), 16, access=mmap.ACCESS_WRITE, offset=16)
# Move to the start of the buffer
mf.seek(0)
# Read a few bytes
print 'Read string:', mf.read(4)
# Close the mmap and the underlying file
mf.close()
f.close()

print '-'*60

