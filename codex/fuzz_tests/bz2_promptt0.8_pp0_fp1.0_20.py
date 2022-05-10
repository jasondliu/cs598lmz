import bz2
# Test BZ2Decompressor

def test_BZ2Decompressor():
    with open(test_support.TESTFN, "wb") as f:
        f.write(bz2.compress(b"this is a test of the bz2 module."))

    with open(test_support.TESTFN, "rb") as f:
        d = bz2.BZ2Decompressor()
        data = []
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            data.append(d.decompress(chunk))
        data.append(d.flush())
        assert b''.join(data) == b"this is a test of the bz2 module."


def test_BZ2Decompressor_read():
    with open(test_support.TESTFN, "wb") as f:
        f.write(bz2.compress(b"this is a test of the bz2 module."))

    with open(test_support.TESTFN, "rb") as f:
        d = bz2.
