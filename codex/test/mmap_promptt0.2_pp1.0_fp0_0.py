import mmap
# Test mmap.mmap.read_byte()

# Create a file and memory-map it
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("hello.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
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
    print(m.read_byte())
    print(m.read_byte())
