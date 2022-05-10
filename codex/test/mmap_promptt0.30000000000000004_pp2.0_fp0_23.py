import mmap
# Test mmap.mmap(fd, length, access=ACCESS_READ)
with open(filename, "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.read(10))
    print(m[:10])
    print(m[10:20])
    print(m[-10:])
    print(m[-10:10])
    print(m[-10:0])
    print(m[-10:1])
    print(m[-10:9])
    print(m[-10:10])
    print(m[-10:11])
    m.close()

# Test mmap.mmap(fileno, length, tagname=None, access=ACCESS_DEFAULT, offset=0)
with open(filename, "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print(m.read(10))
    print(m[:10])
    print
