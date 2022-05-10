import mmap
# Test mmap.mmap size
f = open('data.txt', 'w+')
f.write('\x00' * mmap.PAGESIZE * 2)
f.close()

f = open('data.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
print 'Before:', m.size(), m[0], m[0:3]
m.resize(mmap.PAGESIZE // 2)
print 'After:', m.size(), m[0], m[0:3]
m.close()
f.close()

# Test mmap.mmap offset
f = open('data.txt', 'w+')
f.write('\x00' * mmap.PAGESIZE * 2)
f.close()

f = open('data.txt', 'r+')
m = mmap.mmap(f.fileno(), mmap.PAGESIZE * 2, offset=mmap.PAGESIZE)
print 'Before:', m.size(), m[0], m[0:3]
m.resize(mmap.
