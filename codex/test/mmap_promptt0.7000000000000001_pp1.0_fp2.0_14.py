import mmap
# Test mmap.mmap.write
m = mmap.mmap(1, 1)
m.write('a')
m.write('bcd')
m.close()
# Test mmap.mmap.read
m = mmap.mmap(1, 1)
m.write('a')
m.read(1)
m.close()
# Test mmap.mmap.read
m = mmap.mmap(1, 1)
m.write('a')
m.read(2)
m.close()
# Test mmap.mmap.size
m = mmap.mmap(1, 1)
m.write('a')
m.size()
m.close()
