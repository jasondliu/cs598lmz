import mmap
# Test mmap.mmap(0, size) with various sizes.
# This tests memory protection.
# Note: The memory protection only works in Windows.

for size in [1, 2, 3, 9, 10, 11]:
    print("Testing size", size)
    m = mmap.mmap(-1, size)
    m.write(b'\xff' * size)
    m.flush()  # If memory is not read-only, this will raise an exception.
