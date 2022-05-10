import mmap
# Test mmap.mmap()

# Create a file to test with.
f = open('test.dat', 'w+')
f.write('\x00' * mmap.PAGESIZE)
f.close()

# Open the file and mmap it.
f = open('test.dat', 'r+')
m = mmap.mmap(f.fileno(), 0)

# Write to the mmap'ed file.
m.write('foo')

# Move to the beginning of the mmap'ed file.
m.seek(0)

# Read from the mmap'ed file.
