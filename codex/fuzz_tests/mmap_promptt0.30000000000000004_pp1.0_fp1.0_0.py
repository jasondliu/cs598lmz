import mmap
# Test mmap.mmap()
f = open(filename, 'r+b')
m = mmap.mmap(f.fileno(), 0)
m.write(b'0123456789abcdef')
m.seek(5)
print(m.read(1))
m.seek(6)
m.write(b'Q')
m.close()
f.close()

# Test mmap.mmap() with offset
f = open(filename, 'r+b')
m = mmap.mmap(f.fileno(), 16, offset=8)
m.write(b'0123456789abcdef')
m.seek(5)
print(m.read(1))
m.seek(6)
m.write(b'Q')
m.close()
f.close()

# Test mmap.mmap() with size
f = open(filename, 'r+b')
m = mmap.mmap(f.fileno(), 8)
m.write(b'0123456789abcdef')
m.seek(5)
print(m.read
