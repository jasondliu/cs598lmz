import mmap
# Test mmap.mmap capabilities
m = mmap.mmap(-1, 512)
m[0:8] = 'abcefgh'
# Get an empty space
m[256:] = '\0' * 256
# This will always succeed, 
# even if the file does not exist
file = open('/tmp/test.txt', 'r+b')
mf = mmap.mmap(file.fileno(), 1024)
mf[0:8] = m[0:8]
mf.flush()

# with mmap gurantees it will be closed properly
with mmap.mmap(-1, 512, access=mmap.ACCESS_READ) as m:
    print m
    print len(m)
    print bool(m)
    print m[0]

# Indexing
print 'Before:', m[0]
print 'After :', m[0:1]
m[0] = 'B'
print 'mmap :', m[0]

# Slicing
m[2:5] = 'CDE'
print m.size(), m
