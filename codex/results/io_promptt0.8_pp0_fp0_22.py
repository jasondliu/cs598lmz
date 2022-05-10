import io
# Test io.RawIOBase


class BytesIO(io.BytesIO):

    def read(self, *args, **kw):
        if len(args) == 2 and (args[0] or args[1]):
            raise ValueError
        return io.BytesIO.read(self, *args, **kw)


def test_read():
    rawio = BytesIO(b"abcdefg")
    assert rawio.read(1) == b"a"
    assert rawio.read(5) == b"bcdef"
    assert rawio.read() == b"g"
    assert rawio.read() == b""


def test_bad_read():
    rawio = BytesIO(b"abcdefg")
    with pytest.raises(ValueError):
        rawio.read(0, 5)


def test_readinto():
    b = bytearray(b"abcdefg")
    rawio = BytesIO(b"abcdefg")
    assert rawio.readinto(b) == 7
    assert b == b"abcdefg"
