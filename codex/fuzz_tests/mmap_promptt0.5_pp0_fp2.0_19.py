import mmap
# Test mmap.mmap

with open("test.txt", "wb") as f:
    f.write(b'Hello Python!')

with open("test.txt", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.readline())
    m.close()

# Test mmap.mmap

with open("test.txt", "wb") as f:
    f.write(b'Hello Python!')

with open("test.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.readline())
    m.seek(0)
    m.write(b'Hello World!')
    m.seek(0)
    print(m.readline())
    m.close()

# Test mmap.mmap

with open("test.txt", "wb") as f:
    f.write(b'Hello Python!')

with open("test.txt", "r+b
