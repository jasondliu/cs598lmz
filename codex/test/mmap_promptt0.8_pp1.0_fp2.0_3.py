import mmap
# Test mmap.mmap(fileno, length)
MAX_SIZE = 10 * mmap.ALLOCATIONGRANULARITY
with open(__file__, "r") as f:
    m = mmap.mmap(f.fileno(), MAX_SIZE, access=mmap.ACCESS_READ)
    assert m.size() == MAX_SIZE
    m.close()

# Test mmap.mmap(fileno, length, prot, flags)
with open(__file__, "r") as f:
    m = mmap.mmap(f.fileno(), MAX_SIZE,
                  mmap.ACCESS_READ, mmap.MAP_SHARED)
    assert m.size() == MAX_SIZE
    m.close()

