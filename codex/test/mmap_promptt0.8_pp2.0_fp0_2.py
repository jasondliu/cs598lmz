import mmap
# Test mmap.mmap() with file descriptor, see 
# https://bugs.python.org/issue9019

def test_file_mmap():
    with open(test.support.TESTFN, "wb") as f:
        f.write(b"1234567890")
    with open(test.support.TESTFN, "rb") as f:
        fd = f.fileno()
        m = mmap.mmap(fd, 10, access=mmap.ACCESS_WRITE)
        m[5] = b'Q'
        m.close()

    with open(test.support.TESTFN, "rb") as f:
        data = f.read()
    os.remove(test.support.TESTFN)
    assert data == b"12345Q7890"

def test_file_mmap_with_fileno():
    with open(test.support.TESTFN, "wb") as f:
        f.write(b"1234567890")
