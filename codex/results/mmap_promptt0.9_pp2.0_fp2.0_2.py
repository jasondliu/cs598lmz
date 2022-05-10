import mmap
# Test mmap.mmap
m = mmap.mmap(0, 4096)
print m, len(m) # The length of a mapped 0-page is 4096.
m[0] = '#'
print m[0]
m.seek(0)
print m.read(1), m.tell()
m[2:20] = '#' * 18
print m[:], len(m), m.size(), m.closed, m.mode
m[:20] = '$' * 20
m.seek(0)
m.write('\xfe\x00')
m.seek(0)
print m.read(4)
m.seek(0, 0)
print m.read(4)
m[20:21] = '\xff\x00'
m.seek(20)
print m.read(10), m.tell()
m.close()
print m.closed
m.seek(5)
try:
    print m.read(5)
except ValueError, e:
    print e

m = mmap.mmap(-1, 4096)
print m
