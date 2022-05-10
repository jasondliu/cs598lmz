import mmap
# Test mmap.mmap.read_byte()

# Read the entire file as a single byte string
with open('lorem.txt', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
    print(m.read_byte())
