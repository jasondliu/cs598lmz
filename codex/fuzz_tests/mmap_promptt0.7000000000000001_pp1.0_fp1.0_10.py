import mmap
# Test mmap.mmap.read()
# source: https://docs.python.org/3/library/mmap.html
# usage: python python_mmap_read.py

# Create a file to memory map
with open("python_mmap_read.py.bak", "wb") as f:
    # Write a few bytes to the file
    f.write(b"Hello Python!\n")

print("mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)")
with open("python_mmap_read.py.bak", "rb") as f:
    # Memory-map a file, size 0 means whole file
    # 'f.fileno()' gets the file's file descriptor
    # '0' means whole file
    # 'access=mmap.ACCESS_READ' means read-only
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print("len(m):", len(m))
    print(m.readline())
    print(m.readline
