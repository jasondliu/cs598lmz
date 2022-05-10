import mmap
# Test mmap.mmap()
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
m.write(b'0123456789abcdef')
m.seek(5)  # Go to the 6th byte in the file
print(m.read(1))
m.seek(0)
print(m.read(1))
m.close()
f.close()

# Test mmap.mmap() with length
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 16)
print(m.read(1))
m.close()
f.close()

# Test mmap.mmap() with offset
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 16, access=mmap.ACCESS_WRITE, offset=16)
m.write(b'0123456789abcdef')
m.seek(0)
