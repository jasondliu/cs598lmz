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

# Test mmap.ACCESS_WRITE
print("<test 5>")
try:
    m = mmap(-1, 256)
    m.write("abc")
    m = mmap(m.fileno(), 256, access=ACCESS_WRITE)
    m[2] = "C"
    assert(m[2] == "C")
except TypeError, e:
    print("TypeError:", e)

# Test mmap.find
print("<test 6>")
m = mmap(-1
