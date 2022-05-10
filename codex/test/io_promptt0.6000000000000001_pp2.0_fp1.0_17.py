import io
# Test io.RawIOBase.

with io.BytesIO() as f:
    assert f.read(1) == b''
    f.write(b'abc')
