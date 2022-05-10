import mmap
# Test mmap.mmap(mmap.ACCESS_READ)
with open("dataset.csv", "r") as f:
    m = mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ)
    last = 0
    print('\nMemory-mapped document:')
    print(m.read(5))
    print('\nSame as regular file:')
    print(m[0:5])
    m.seek(0)
    while True:
        line = m.readline()
        if not line: break
        last = m.tell()
        print (line[:-1])
    m.close()

# Example of memory-mapped file IO with mmap
with open("dataset2.csv", "r") as f:
    m = mmap.mmap(f.fileno(), 0)
    print('\nMemory-mapped document:')
    print(m.read(5))
    m.seek(0)
