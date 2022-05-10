import mmap
# Test mmap.mmap.read()
mem = mmap.mmap(1, 10, mmap.ACCESS_READ)
try:
    mem.read()
except TypeError:
    print("TypeError")

# Test mmap.mmap.read()
mem = mmap.mmap(1, 10, mmap.ACCESS_READ)
try:
    mem.read(0)
except TypeError:
    print("TypeError")

# Test mmap.mmap.read()
mem = mmap.mmap(1, 10, mmap.ACCESS_READ)
try:
    mem.read(0, 2)
except TypeError:
    print("TypeError")

# Test mmap.mmap.read()
