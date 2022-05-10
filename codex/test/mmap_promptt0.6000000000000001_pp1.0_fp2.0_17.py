import mmap
# Test mmap.mmap with a large file.

# Make a big file.

def test_large_file():
    f = open("largefile", "wb")
    f.seek(100000000)
    f.write(b"\0")
    f.close()

    f = open("largefile", "r+b")

    # Map it.
    m = mmap.mmap(f.fileno(), 0)

    # Write to the start of the file.
    m[0:10] = b"0123456789"

    # Write to the end of the file.
    m[-10:] = b"9876543210"

    # Write to the middle of the file.
    m[40000000:40000010] = b"abcdefghij"

    f.close()

    f = open("largefile", "rb")
    m = mmap.mmap(f.fileno(), 0)
    assert m[0:10] == b"0123456789"
    assert m[-10:] == b"9876543210"
