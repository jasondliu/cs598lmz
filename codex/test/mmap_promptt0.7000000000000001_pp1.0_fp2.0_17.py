import mmap
# Test mmap.mmap(-1, 13) with a 13-byte string.
# It should not throw an error, but should return a 13-byte array.

m = mmap.mmap(-1, 13)
m.write(b"Hello, world!\n")
m.seek(0)
