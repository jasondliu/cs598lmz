import mmap
# Test mmap.mmap
with open('somefile', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print 'First 10 bytes via read :', m.read(10)
        print 'First 10 bytes via slice:', m[:10]
        print '2nd   10 bytes via read :', m.read(10)

# Test mmap.mmap with offset
with open('somefile', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print 'First 10 bytes via read :', m.read(10)
        print 'First 10 bytes via slice:', m[:10]
        print '2nd   10 bytes via read :', m.read(10)

# Test mmap.mmap with size
with open('somefile', 'r') as f:
    with mmap.mmap(f.fileno(), mmap.PAGESIZE, access=mmap.ACCESS_READ) as
