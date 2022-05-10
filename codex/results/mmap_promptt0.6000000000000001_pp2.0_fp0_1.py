import mmap
# Test mmap.mmap
with open("test.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.readline())
    print(m[:5])

# Test mmap.mmap()
import os
with open("test.txt", "w+b") as f:
    f.write(b"Hello Python!\nGoodbye Python!")
    f.seek(0)
    m = mmap.mmap(f.fileno(), 0)
    print(m.readline())
    print(m[:5])

# Test mmap.mmap(0, size)
with open("test.txt", "w+b") as f:
    f.write(b"Hello Python!\nGoodbye Python!")
    f.seek(0)
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(m.readline())
    print(m[:5])
    m.seek(0)
    m.
