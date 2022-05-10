import io
# Test io.RawIOBase.

with io.BytesIO() as f:
    assert f.read(1) == b''
    f.write(b'abc')
    assert f.read(1) == b'a'
    assert f.read(1) == b'b'
    assert f.read(1) == b'c'
    assert f.read(1) == b''
    f.write(b'def')
    assert f.read(1) == b'd'
    f.seek(0)
    assert f.read(1) == b'a'

with io.BytesIO(b'abc') as f:
    assert f.read(1) == b'a'
    assert f.read(1) == b'b'
    assert f.read(1) == b'c'
    assert f.read(1) == b''

# Test io.BufferedIOBase.

with io.BytesIO() as f:
    assert f.read(1) == b''
    f.write(b'abc')
    assert f.read(1)
