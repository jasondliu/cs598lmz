import mmap
# Test mmap.mmap.flush
print('mmap.mmap flush')
fp = open('mmap.mmap', 'wb+')
print('mmap.mmap.flush', mmap.mmap(fp.fileno(), 0).flush())

# Test mmap.mmap.close
print('mmap.mmap close')
fp = open('mmap.mmap', 'wb+')
print('mmap.mmap.close', mmap.mmap(fp.fileno(), 0).close())

# Test mmap.mmap.find
print('mmap.mmap find')
fp = open('mmap.mmap', 'wb+')
print('mmap.mmap.find', mmap.mmap(fp.fileno(), 0).find(b'abc'))
print('mmap.mmap.find', mmap.mmap(fp.fileno(), 0).find(b'abc', 1))

# Test mmap.mmap.move
print('mmap.mmap move')
fp = open('mmap.mmap', 'wb+')
print('mmap
