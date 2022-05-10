import mmap
# Test mmap.mmap(-1, 0)
with pytest.raises(TypeError):
    mmap.mmap(-1, 0)
with pytest.raises(ValueError):
    mmap.mmap(0, -1)
with pytest.raises(ValueError):
    mmap.mmap(0, 1, access=mmap.ACCESS_WRITE)

# test range param
with tempfile.TemporaryFile() as f:
    m = mmap.mmap(f.fileno(), 0, offset=0, length=1)
    assert m[0] == 0
    assert m.size() == 1

with tempfile.TemporaryFile() as f:
    m = mmap.mmap(f.fileno(), 0, offset=2, length=1)
    assert m.size() == 1

with tempfile.TemporaryFile() as f:
    m = mmap.mmap(f.fileno(), 0, offset=0, length=3)
    assert m.size() == 3

with tempfile.TemporaryFile() as f:

