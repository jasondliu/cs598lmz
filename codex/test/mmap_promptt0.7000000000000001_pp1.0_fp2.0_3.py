import mmap
# Test mmap.mmap.readline
with open("largefile", "w+b") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print("0:", m.readline())
    print("1:", m.readline())
    print("2:", m.readline())
    print("3:", m.readline())
    m.seek(0, 0)
    print("0:", m.readline())
    print("1:", m.readline())
    print("2:", m.readline())
    print("3:", m.readline())
    m.close()

# Test mmap.mmap.readlines
with open("largefile", "w+b") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print("0:", m.readlines())
    print("1:", m.readlines())
    print("2:", m.readlines())
