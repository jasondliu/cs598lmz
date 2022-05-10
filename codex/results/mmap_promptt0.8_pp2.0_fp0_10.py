import mmap
# Test mmap.mmap() does not segfault on zero-sized files.
with open("mmap_test", "wb") as fp:
    pass
with open("mmap_test", "rb") as fp:
    mmap.mmap(fp.fileno(), 0)
os.unlink("mmap_test")

# test that mmap objects are usable with array.array constructor
import os
import mmap
import array

f = open("mmap_array", "wb")
try:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    try:
        a = array.array("B", mm)
        assert a[0] == 0, "array initialized from mmap should be filled with zeros"
    finally:
        mm.close()
finally:
    f.close()
os.unlink("mmap_array")

# test that mmap doesn't crash when asked to map a region larger than
# the file.
import os
import mmap

f = open("mmap_excess",
