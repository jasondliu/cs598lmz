import io
# Test io.RawIOBase.readinto()

import _io

buf = bytearray(b'x' * 10)

for i in range(len(buf)):
    with _io.BytesIO(b'x' * i) as f:
        n = f.readinto(buf)
        assert n == i
        assert buf[:n] == b'x' * i
        assert buf[n:] == b'x' * (len(buf) - n)


with _io.BytesIO(b'x' * 10) as f:
    n = f.readinto(buf)
    assert n == len(buf)
    assert buf == b'x' * len(buf)
    assert f.readinto(buf) == 0

with _io.BytesIO(b'x' * 10) as f:
    n = f.readinto(memoryview(buf))
    assert n == len(buf)
    assert buf == b'x' * len(buf)
    assert f.readinto(memoryview(buf)) == 0

