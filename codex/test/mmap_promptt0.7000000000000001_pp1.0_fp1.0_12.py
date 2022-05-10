import mmap
# Test mmap.mmap(0, 1)

with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("hello.txt", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.find(b"Python"))
    print(m.find(b"Qt"))
