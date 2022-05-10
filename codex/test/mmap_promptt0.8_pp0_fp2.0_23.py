import mmap
# Test mmap.mmap(2)
with open("/tmp/test.mmap", "wb") as file:
    file.write(b"a" * mmap.ALLOCATIONGRANULARITY)
with mmap.mmap(file.fileno(), mmap.ALLOCATIONGRANULARITY) as m:
    assert m.read(1) == b"a"
    assert m.size() == mmap.ALLOCATIONGRANULARITY
    m.resize(2 * mmap.ALLOCATIONGRANULARITY)
    assert m.size() == 2 * mmap.ALLOCATIONGRANULARITY
    m.write(b"b" * mmap.ALLOCATIONGRANULARITY)
    assert m.read(mmap.ALLOCATIONGRANULARITY) == b"b" * mmap.ALLOCATIONGRANULARITY

# Test mmap.mmap(-1, ...) aka mmap.mmap(-1, ..., mmap.MAP_ANONYMOUS)
