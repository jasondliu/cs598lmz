import mmap
# Test mmap.mmap.find()

# Make a memory map to an empty file, and write some data to it.
filename = support.TESTFN
fp = open(filename, 'w+b')
fp.write(b'\x00\x00\x00\x00\x00\x00')
m = mmap.mmap(fp.fileno(), 6)
m[4:] = b'abcd'
m.close()
fp.close()

# Get a new reference to the file
fp = open(filename, 'r+b')
m = mmap.mmap(fp.fileno(), 6)

# find() should return the first index of the pattern
pos = m.find(b'cd')
assert pos == 4, 'find() returned wrong position'

pos = m.find(b'xy')
assert pos == -1, 'find() returned wrong position'

# The pattern must be a string.
try:
    m.find(42)
except TypeError:
    pass
else:
    raise Exception('expected TypeError')

# An integer can be provided
