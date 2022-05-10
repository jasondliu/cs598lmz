import mmap
# Test mmap.mmap(-1, 1) on windows
# This will cause a call to CreateFileMapping() with a NULL name
# The documentation says this is illegal, but it seems to work
m = mmap.mmap(-1, 1)
print m
m.close()
