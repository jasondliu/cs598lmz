import mmap
# Test mmap.mmap()
with open("sample.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 0)
    print("mmap.mmap()\n", m)
    print("m[0:13]\n", m[0:13])
    m.close()

# Test mmap.mmap(fileno, length, flags, prot, access, offset)
with open("sample.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 13, access=mmap.ACCESS_WRITE)
    print("mmap.mmap(fileno, length, flags, prot, access, offset)\n", m)
    print("m[0:13]\n", m[0:13])
    m.close()

# Test mmap.mmap(fileno, length, flags, prot, access, offset)
with open("sample.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 13,
                  access=mmap.ACCESS
