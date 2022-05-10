import mmap
# Test mmap.mmap(0, 1, "mymmap")
# Test mmap.mmap(-1, 1, "mymmap")

# Check that invalid offsets are caught.
try:
    mmap.mmap(-1, 1, "mymmap", offset=1)
except ValueError:
    pass
else:
    print("Failed to raise ValueError with invalid offset")

# Check that invalid lengths are caught.
try:
    mmap.mmap(-1, -1, "mymmap", offset=1)
except ValueError:
    pass
else:
    print("Failed to raise ValueError with invalid length")

# Check that invalid access parameters are caught.
