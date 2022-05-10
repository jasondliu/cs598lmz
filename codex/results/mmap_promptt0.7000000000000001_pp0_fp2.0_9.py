import mmap
# Test mmap.mmap
with open("test_mmap.txt", "wb") as f:
    f.write(b"Hello Python!\n")
with open("test_mmap.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    print(f"Before: {m.readline()}")
    m.seek(0)
    m.write(b"Hello World!\n")
    m.seek(0)
    print(f"After: {m.readline()}")
    m.close()

# Test mmap.ACCESS
with open("test_mmap.txt", "wb") as f:
    f.write(b"Hello Python!\n")
with open("test_mmap.txt", "r+b") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.seek(0)
    print(f"Before: {m.readline()}")

