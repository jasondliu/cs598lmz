import mmap
# Test mmap.mmap function
mmap.mmap(1, 0x100)

# CHECK: Traceback
# CHECK: UnsupportedOperation: mmap.mmap does not work on Windows
# CHECK: ImportError
