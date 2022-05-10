import mmap
# Test mmap.mmap
mem = mmap.mmap(-1, 100)
mem.write(b'aaaaaaaaaaa')
mem[3:8]
mem.seek(5)
mem.write(b'x')
mem.close()

# Test mmap.mmap with a file
f = open('foo.txt', 'wb')
f.write(bytes(100))
f.close()
f = open('foo.txt', 'r+b')
m = mmap.mmap(f.fileno(), 100, access=mmap.ACCESS_WRITE)
m.write(b'i')
m.readline()
m.close()
f.close()
