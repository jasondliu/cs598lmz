import mmap
# Test mmap.mmap() errors
try:
    mmap.mmap(-1, 1)
except ValueError:
    pass
else:
    print("ValueError expected")

try:
    mmap.mmap(0, 0)
except ValueError:
    pass
else:
    print("ValueError expected")

try:
    mmap.mmap(1, 0, access=mmap.ACCESS_WRITE)
except ValueError:
    pass
else:
    print("ValueError expected")

try:
    mmap.mmap(1, 0, access=1)
except ValueError:
    pass
else:
    print("ValueError expected")

try:
    mmap.mmap(1, 0, access=mmap.ACCESS_READ, flags=-1)
except ValueError:
    pass
else:
    print("ValueError expected")

try:
    mmap.mmap(1, 0, access=mmap.ACCESS_READ, prot=-1)
except ValueError:
    pass
else:
    print("ValueError expected")

