import mmap
# Test mmap.mmap(-1, 0)

with open("/proc/self/maps", "r") as f:
    maps0 = f.read()

m = mmap.mmap(-1, 0)

with open("/proc/self/maps", "r") as f:
    maps1 = f.read()

# New mapping should be created
assert maps1 != maps0

# Test mmap.mmap(-1, 0, mmap.PROT_WRITE)

with open("/proc/self/maps", "r") as f:
    maps0 = f.read()

m = mmap.mmap(-1, 0, mmap.PROT_WRITE)

with open("/proc/self/maps", "r") as f:
    maps1 = f.read()

# New mapping should be created
assert maps1 != maps0

# Test mmap.mmap(-1, 0, mmap.MAP_SHARED)

with open("/proc/self/maps", "r") as f:
    maps0 = f.read()


