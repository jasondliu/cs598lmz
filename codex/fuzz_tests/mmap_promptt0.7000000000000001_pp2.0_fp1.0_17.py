import mmap
# Test mmap.mmap.read_byte()

m = mmap.mmap(-1, 1024)
m[3] = b'\x00'
m.read_byte()
# Read from offset 3
print(m.read_byte())
m.close()
