import mmap
# Test mmap.mmap() with a negative length;
# This should raise a ValueError
try:
    mm = mmap.mmap(-1, 1)
except ValueError:
    print("ValueError")
