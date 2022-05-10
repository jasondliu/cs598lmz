import mmap
# Test mmap.mmap(0, 1)
for i in range(1, 100000):
    try:
        m = mmap.mmap(0, i)
    except OverflowError:
        break
    del m
# Test mmap.mmap(0, 1, mmap.MAP_SHARED, mmap.PROT_READ|mmap.PROT_WRITE, 0)
for i in range(1, 100000):
    try:
        m = mmap.mmap(0, i, mmap.MAP_SHARED, mmap.PROT_READ|mmap.PROT_WRITE, 0)
    except OverflowError:
        break
    del m
# Test mmap.mmap(0, 1, mmap.MAP_SHARED, mmap.PROT_READ|mmap.PROT_WRITE, 1)
for i in range(1, 100000):
    try:
        m = mmap.mmap(0, i, mmap.MAP_SHARED, mmap.PROT_READ|mmap.PROT_WRITE
