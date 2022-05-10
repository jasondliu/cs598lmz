import mmap
# Test mmap.mmap
print("<test 3>")
m = mmap.mmap(-1, 256)
m.write("abc")
assert(m[2] == "c")

from mmap import mmap, ACCESS_READ, ACCESS_WRITE
from os import close
# Test mmap.ACCESS_READ
print("<test 4>")
m = mmap(-1, 256)
m.write("abc")
m = mmap(m.fileno(), 256, access=ACCESS_READ)
assert(m[2] == "c")

