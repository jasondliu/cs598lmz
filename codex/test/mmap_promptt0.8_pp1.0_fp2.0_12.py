import mmap
# Test mmap.mmap() constructor.
# It does not work under Windows, even though the documentation claims
# otherwise.

fname = "mmap_mm_test.txt"
with open(fname, 'w+') as f:
    f.write('0123456789')
with open(fname) as f:
    mm = mmap.mmap(f.fileno(), 10, access=mmap.ACCESS_READ)
    assert mm[:] == b'0123456789'
import mmap
# Test mmap.mmap() constructor with defaults.
# It does not work under Windows, even though the documentation claims
# otherwise.

fname = "mmap_mm_test.txt"
with open(fname, 'w+') as f:
    f.write('0123456789')
with open(fname) as f:
    mm = mmap.mmap(f.fileno())
    assert mm[:] == b'0123456789'
import mmap
