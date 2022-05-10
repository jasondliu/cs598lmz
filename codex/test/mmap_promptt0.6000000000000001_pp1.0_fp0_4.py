import mmap
# Test mmap.mmap()
#
# This test ensures that mmap.mmap() can be used to create an mmap object
# from a file descriptor, which is useful for mmapping files opened by
# os.open().
#
with open(TESTFN, "wb") as f:
    f.write(b"\x00" * 100)
with open(TESTFN, "rb") as f:
    fd = f.fileno()
    with mmap.mmap(fd, 100) as m:
        m[0] = b"\x01"
with open(TESTFN, "rb") as f:
    assert f.read(1) == b"\x01"
    assert f.read(99) == b"\x00" * 99
# Test mmap.mmap() errors
#
# This test ensures that mmap.mmap() raises ValueError when the length
# is negative or when the offset is negative or greater than the file
# size.
