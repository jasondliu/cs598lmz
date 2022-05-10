import mmap
# Test mmap.mmap
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
m.write('0123456789abcdef')
m.seek(5)
print m.read(1)
m.seek(0)
print m.read(10)
m.seek(16)
m.write('ABCDEF')
m.seek(0)
print m.read(16)
m.close()
f.close()

# Test mmap.mmap with offset
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0, offset=5)
print m.read(1)
m.seek(0)
print m.read(10)
m.seek(16)
m.write('ABCDEF')
m.seek(0)
print m.read(16)
m.close()
f.close()

# Test mmap.mmap with size
f = open('test.txt', 'r+')
m = mmap.mmap(f.fil
