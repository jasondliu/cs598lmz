import io
# Test io.RawIOBase.readinto() with buffer of various sizes, including
# non-native-size buffers.
import _io

def test_readinto_1():
    import _io
    r = _io.BytesIO(b"12345678")
    for n in range(1, 9):
        buf = bytearray(n)
        m = r.readinto(buf)
        assert m == n
        assert buf == b"".join([bytes([c]) for c in range(1, n+1)])
        buf = bytearray(n)
        m = r.readinto(buf)
        assert m == 0
        assert buf == bytearray(n)

    r = _io.BytesIO(b"12345678")
    for n in range(1, 9):
        buf = bytearray(n+1)
        m = r.readinto(buf)
        assert m == n
        assert buf == b"".join([bytes([c]) for c in range(1, n+1)]) + b'\x00'
        buf = by
