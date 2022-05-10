import mmap
# Test mmap.mmap()
m = mmap.mmap(fd, 0)
m # should print <mmap closed file 'parcels.0.0.nc', 2560000 bytes>
print m.size
# Test mmap[offset:offset+1]
m[0:1] # should print '='
m[1:2] # should print 'C'
m[2:3] # should print 'D'
m[3:4] # should print 'D'
m[4:5] # should print 'H'
# Test mmap[offset]
m[0]   # should print '='
m[1]   # should print 'C'
m[2]   # should print 'D'
m[3]   # should print 'D'
m[4]   # should print 'H'
m.close()

# Test os.fdopen()
fd = os.open(infile, os.O_RDONLY)
fd # should print a file descriptor number, e.g. 3
f = os.fdopen(fd)
f # should print <open file 'parcel
