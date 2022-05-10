import mmap
# Test mmap.mmap(0, length, 'MAP_NORESERVE', 'MAP_ANONYMOUS', 'MAP_PRIVATE')
# https://github.com/python/cpython/blob/3.7/Modules/mmapmodule.c#L1878
# TODO: Test mmap.mmap(-1, length, 'MAP_NORESERVE', 'MAP_ANONYMOUS', 'MAP_PRIVATE', 0, fd)
# https://github.com/python/cpython/blob/3.7/Modules/mmapmodule.c#L1883

#
# Basic mapping
#

length = 65536
m = mmap.mmap(-1, length)  # no-op, just returns the raw buffer
if PY3:
    assert m[:5] == b'\x00' * 5  # Looking at a raw buffer
    assert m.read(5) == b'\x00' * 5  # Read raw buffer as bytes
    # Cannot read as text
    with pytest.raises(TypeError):
        m.read_
