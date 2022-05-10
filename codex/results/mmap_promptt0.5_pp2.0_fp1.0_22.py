import mmap
# Test mmap.mmap.read_byte()

# Read the first byte of the file
with open("lorem.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    print("First byte:", m.read_byte())
    m.close()

# Read the first byte of the file
with open("lorem.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    print("First byte:", m[0])
    m.close()

# Read the first byte of the file
with open("lorem.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    print("First byte:", m.read(1))
    m.close()

# Read the first byte of the file
with open("lorem.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    print("First byte:", m.read(1)[0])
