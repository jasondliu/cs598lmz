import mmap
# Test mmap.mmap(-1, 13) with a 13-byte string.
# It should not throw an error, but should return a 13-byte array.

m = mmap.mmap(-1, 13)
m.write(b"Hello, world!\n")
m.seek(0)
if m.read(13) != b"Hello, world!\n":
    raise TestFailed("mmap.mmap(-1, 13) failed")
print("Test passed.")

m.close()
