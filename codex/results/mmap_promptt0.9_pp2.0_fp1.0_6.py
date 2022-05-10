import mmap
# Test mmap.mmap of a file and mmap.mmap of an mmap.
result = 0
f = open(tempfile.mktemp(), 'wb+', 0777)
f.write(' ' * mmap.PAGESIZE)
m1 = mmap.mmap(f.fileno(), mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE)
m2 = mmap.mmap(m1.fileno(), mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset=0)
# make sure m1 and m2 have the same content.
assert m1[0:1] == m2[0:1]
m2.flush(offset=1, size=1)
m1.write('a')
m1.flush(size=1)
assert m1[1:2] == m2[1:2]
m2.close()
m1.close()
f.close()
print 'ok'


