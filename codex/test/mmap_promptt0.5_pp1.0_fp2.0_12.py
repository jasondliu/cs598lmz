import mmap
# Test mmap.mmap.read(1) with offset.
#
# This test was contributed by Victor Stinner

with open('mmap_read_1_offset.dat', 'wb') as f:
    f.write(b'x' * 1024)

with open('mmap_read_1_offset.dat', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    for i in range(1024):
        assert m.read(1) == b'x'
    m.close()
