import mmap
# Test mmap.mmap
fh = open('mmapfile', 'w+')
fh.write('01234567890123456789')

m = mmap.mmap(fh.fileno(), 0)
