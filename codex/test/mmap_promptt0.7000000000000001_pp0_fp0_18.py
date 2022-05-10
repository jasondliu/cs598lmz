import mmap
# Test mmap.mmap() for read and write

print("test mmap.mmap() for read and write")
with open("test_mmap", "w+b") as fp:
    # length must be a multiple of mmap.ALLOCATIONGRANULARITY
    fp.write(b"\x00"*mmap.ALLOCATIONGRANULARITY)

with open("test_mmap", "r+b") as fp:
    m = mmap.mmap(fp.fileno(), 0)
    m[0:mmap.ALLOCATIONGRANULARITY] = b"\xFF"*mmap.ALLOCATIONGRANULARITY
    m.flush()
    m.close()

with open("test_mmap", "rb") as fp:
    m = mmap.mmap(fp.fileno(), 0)
    assert m[0:mmap.ALLOCATIONGRANULARITY] == b"\xFF"*mmap.ALLOCATIONGRANULARITY
    m.close()

