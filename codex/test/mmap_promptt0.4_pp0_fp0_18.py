import mmap
# Test mmap.mmap.read_byte()
m = mmap.mmap(-1, 1)
m.write(b'\x00')
m.read_byte()

# Test mmap.mmap.read()
m = mmap.mmap(-1, 1)
m.write(b'\x00')
m.read()

# Test mmap.mmap.readline()
m = mmap.mmap(-1, 1)
m.write(b'\x00')
m.readline()

# Test mmap.mmap.readlines()
m = mmap.mmap(-1, 1)
m.write(b'\x00')
m.readlines()

# Test mmap.mmap.seek()
m = mmap.mmap(-1, 1)
m.write(b'\x00')
m.seek(0)

# Test mmap.mmap.tell()
m = mmap.mmap(-1, 1)
m.write(b'\x00')
m.tell()

