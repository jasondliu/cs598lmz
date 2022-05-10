import mmap
# Test mmap.mmap

f = open('/tmp/test.txt', 'w+')
f.write('0123456789abcdef')
f.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
print m[:]
m[0] = 'A'
m.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
print m[:]
m[0] = 'B'
m.flush()
m.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
print m[:]
m[:] = 'C'
m.flush()
m.close()

f = open('/tmp/test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
print m[:]
m.close()

f = open('/tmp/test.txt
