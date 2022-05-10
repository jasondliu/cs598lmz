import mmap
# Test mmap.mmap.read_byte()

# Read a byte from a file
with open("test.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read_byte())

# Read a byte from a memory buffer
m = mmap.mmap(-1, 1)
m.write(b"a")
print(m.read_byte())

# Read a byte from a memory buffer
m = mmap.mmap(-1, 1)
m.write(b"a")
print(m.read_byte())

# Read a byte from a memory buffer
m = mmap.mmap(-1, 1)
m.write(b"a")
print(m.read_byte())

# Read a byte from a memory buffer
m = mmap.mmap(-1, 1)
m.write(b"a")
print(m.read_byte())

# Read a byte from a memory buffer
m = mmap.mmap(-1, 1)
m.write(b"a")
print
