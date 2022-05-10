import mmap
# Test mmap.mmap()
with open("sample.txt", "r+") as f:
    m = mmap.mmap(f.fileno(), 0)
    print("mmap.mmap()\n", m)
    print("m[0:13]\n", m[0:13])
    m.close()

