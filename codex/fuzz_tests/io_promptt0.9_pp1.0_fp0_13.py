import io
# Test io.RawIOBase
try:
    fp = open(__file__, 'rb')
    assert isinstance(fp, io.BufferedIOBase)
    assert isinstance(fp, io.RawIOBase)
    assert fp.readable()
    assert fp.read(10) == b"import io\n"
    # seek and read again
    fp.seek(0, 0)
    assert fp.read(10) == b"import io\n"
    # readinto
    fp.seek(0)
    b = bytearray(4)
    p = memoryview(b)
    assert fp.readinto(b) == 4
    assert fp.readinto(b) == 4
    assert fp.readinto(p) == 2
    fp.close()
except OSError:
    pass


# Issue 22397: Test io.RawIOBase is not exported
assert not hasattr(sys, "RawIOBase")


# test invalid args
try:
    io.BytesIO()
except TypeError as e:
    assert str(
