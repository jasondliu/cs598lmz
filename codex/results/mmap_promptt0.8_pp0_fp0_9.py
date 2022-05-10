import mmap
# Test mmap.mmap
d = mmap.mmap(-1,10000)
d.write('0' * 10000)
s = mmap.mmap(-1,10000)
s.write('1' * 10000)
print 'test', s[:] == d[:]
s.close()
d.close()

# Test mmap.mmap
d = mmap.mmap(-1,10000)
d.write('0' * 10000)
s = mmap.mmap(-1,10000)
s.write('1' * 10000)
print 'test', s[0:5] == d[0:5]
s.close()
d.close()

# Test mmap.mmap
d = mmap.mmap(-1,10000)
d.write('0' * 10000)
s = mmap.mmap(-1,10000)
s.write('1' * 10000)
print 'test', s[-5:] == d[-5:]
s.close()
d.close()

# Test mmap.mmap
d = mmap.mmap(-1,10000)

