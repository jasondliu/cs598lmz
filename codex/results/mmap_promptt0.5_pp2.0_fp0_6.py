import mmap
# Test mmap.mmap()
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
m.write('0123456789abcdef')
m.seek(0)
print m.read(16)
m.close()
f.close()

# Test mmap.mmap(-1, ...)
f = open('test.txt', 'r+')
m = mmap.mmap(-1, 1024, access=mmap.ACCESS_READ)
m.write('0123456789abcdef')
m.seek(0)
print m.read(16)
m.close()
f.close()

# Test mmap.mmap(0, ...)
f = open('test.txt', 'r+')
m = mmap.mmap(0, 1024, access=mmap.ACCESS_WRITE)
m.write('0123456789abcdef')
m.seek(0)
print m.read(16)
m.close()
f.close()

# Test mmap.mmap(
