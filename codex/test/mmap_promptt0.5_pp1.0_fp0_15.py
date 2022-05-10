import mmap
# Test mmap.mmap.read_byte()
m = mmap.mmap(-1, 1024)
m.write(b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09")
m.read_byte()

# Test mmap.mmap.read()
m = mmap.mmap(-1, 1024)
m.write(b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09")
m.read(5)

# Test mmap.mmap.readline()
m = mmap.mmap(-1, 1024)
m.write(b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09")
m.readline()

# Test mmap.mmap.resize()
m = mmap.mmap(-1, 1024)
m.resize(2048)
m.size()

