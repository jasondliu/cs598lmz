import mmap
# Test mmap.mmap(-1, 0)
# https://bugs.python.org/issue12293
# https://bugs.python.org/issue12294
with mmap.mmap(-1, 0) as m:
    pass
# Test mmap.mmap(-1, 0, access=mmap.ACCESS_WRITE)
# https://bugs.python.org/issue12293
# https://bugs.python.org/issue12294
with mmap.mmap(-1, 0, access=mmap.ACCESS_WRITE) as m:
    pass
