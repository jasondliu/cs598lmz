import mmap
# Test mmap.mmap
m = mmap.mmap(0, 1, "test")
m.write_byte(b'a')
m.seek(0)
m.read_byte()

# Test mmap.mmap.read
m.seek(0)
m.read(1)

# Test mmap.mmap.write
m.seek(0)
m.write(b'b')

# Test mmap.mmap.write_byte
m.seek(0)
m.write_byte(b'c')
m.seek(0)
m.read_byte()

# Test mmap.mmap.readinto
m.seek(0)
m.write_byte(b'd')
m.seek(0)
m.readinto(bytearray(1))

# Test mmap.mmap.tell
m.tell()

# Test mmap.mmap.seek
m.seek(0)
m.seek(0, 0)
m.seek(0, 1)
m.seek(0, 2)

# Test mmap.
