import mmap
# Test mmap.mmap.read_byte()

# Read from a file
with open("foo.txt", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.read_byte())

# Read from a byte array
m = mmap.mmap(-1, 1)
m.write_byte(65)
print(m.read_byte())

# Read from a string
m = mmap.mmap(-1, 1)
m.write_byte(65)
print(m.read_byte())

# Read from a unicode string
m = mmap.mmap(-1, 1)
m.write_byte(65)
print(m.read_byte())

# Read from a memoryview
m = mmap.mmap(-1, 1)
m.write_byte(65)
print(m.read_byte())

# Read from an array
m = mmap.mmap(-1, 1)
