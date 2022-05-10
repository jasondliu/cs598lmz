import mmap
# Test mmap.mmap()
# Expected result:
# - Memory map is read/write by default.
m = mmap.mmap(-1, 1, "testmmap1")
assert m.size() == 1
assert m.read(1) == "\x00"
m.write("\x01")
assert m.read(1) == "\x01"
m.close()

# Test mmap.mmap(fileno)
# Expected result:
# - Memory map is read/write by default.

# Test mmap.mmap(fileno, size)
# Expected result:
# - Memory map is read/write by default.

# Test mmap.mmap(fileno, size, flags)
# Expected result:
# - Memory map is read/write by default.

# Test mmap.mmap(fileno, size, flags, prot)
# Expected result:
# - Memory map is read/write by default.

# Test mmap.mmap(fileno, size, flags, prot, access)
# Expected result:
# - Memory map is
