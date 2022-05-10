import mmap
# Test mmap.mmap()
with open("test.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("test.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    data = m.readline()
    print(data)
    m[6:12] = b"world"
    m.seek(0)
    data = m.readline()
    print(data)
    m.close()

# Test mmap.mmap(-1, size)
with open("test.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("test.txt", "r+b") as f:
    m = mmap.mmap(-1, 13)
    m.write(b"Hello World!\n")
    m.seek(0)
    data = m.readline()
    print(data)
    m.close()

# Test mmap.mmap(fil
