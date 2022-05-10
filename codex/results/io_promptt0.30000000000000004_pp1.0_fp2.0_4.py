import io
# Test io.RawIOBase

class TestRawIOBase:

    def test_readinto(self):
        # Test reading into a bytearray
        b = bytearray(b"abc")
        f = io.BytesIO(b"xyz")
        n = f.readinto(b)
        assert n == 3
        assert b == b"xyz"

        # Test reading into an array
        import array
        a = array.array('b', b"abc")
        f = io.BytesIO(b"xyz")
        n = f.readinto(a)
        assert n == 3
        assert a.tobytes() == b"xyz"

        # Test reading into a memoryview
        b = bytearray(b"abc")
        f = io.BytesIO(b"xyz")
        m = memoryview(b)
        n = f.readinto(m)
        assert n == 3
        assert b == b"xyz"

        # Test reading into a read-only buffer
        b = bytearray(b"abc")
        f =
