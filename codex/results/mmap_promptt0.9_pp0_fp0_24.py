import mmap
# Test mmap.mmap with anonymous private & shared mapping
m = mmap.mmap(-1, 0x1000, mmap.MAP_PRIVATE|mmap.MAP_ANONYMOUS|mmap.MAP_SHARED)
print(repr(m.read_byte()))  # should return 0


import mmap
# Test mmap.mmap with anonymous private & shared mapping
m = mmap.mmap(-1, 0x1000, mmap.MAP_PRIVATE|mmap.MAP_ANONYMOUS)
print(repr(m.read_byte()))  # should return 0
print("%c"%m.read_byte())  # should return 0
