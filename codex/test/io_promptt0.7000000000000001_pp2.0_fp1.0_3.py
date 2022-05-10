import io
# Test io.RawIOBase.readinto
def test_readinto():
    with io.BytesIO(b"foo") as f:
        b = bytearray(3)
        n = f.readinto(b)
        assert n == 3
        assert b == b"foo"
        # Should read no more than requested.
        n = f.readinto(b)
        assert n == 0
        assert b == b"foo"
    with io.BytesIO(b"foobar") as f:
        b = bytearray(3)
        n = f.readinto(b)
        assert n == 3
        assert b == b"foo"
        # Should read no more than requested.
        n = f.readinto(b)
        assert n == 0
        assert b == b"foo"
    with io.BytesIO(b"") as f:
        b = bytearray(3)
        n = f.readinto(b)
        assert n == 0
        assert b == b"\0\0\0"
        # Should read no more than requested.
       
