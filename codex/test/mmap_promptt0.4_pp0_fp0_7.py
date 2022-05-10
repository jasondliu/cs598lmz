import mmap
# Test mmap.mmap(-1, 2**31)
with mmap.mmap(-1, 2**31) as m:
    m.seek(0, 2)
    assert m.tell() == 0

# Test mmap.mmap(-1, 2**31 + 1)
with mmap.mmap(-1, 2**31 + 1) as m:
    m.seek(0, 2)
    assert m.tell() == 0

# Test mmap.mmap(-1, 2**32)
with mmap.mmap(-1, 2**32) as m:
    m.seek(0, 2)
    assert m.tell() == 0

# Test mmap.mmap(-1, 2**32 + 1)
with mmap.mmap(-1, 2**32 + 1) as m:
    m.seek(0, 2)
    assert m.tell() == 0

# Test mmap.mmap(-1, 2**63 - 1)
