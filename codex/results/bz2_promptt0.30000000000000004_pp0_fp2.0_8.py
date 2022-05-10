import bz2
# Test BZ2Decompressor.__init__() with a file object.

data = b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'

with bz2.open(io.BytesIO(data), 'rb') as f:
    assert f.read() == b'hello'

with bz2.open(io.BytesIO(data), 'rb', 9) as f:
    assert f.read() == b'hello'

with bz2.open(io.BytesIO(data), 'rb', compresslevel=9) as f:
    assert f.read() == b'hello'

with bz2.open(io.BytesIO(data), 'rb', compresslevel=9,
              encoding='latin-1') as f:
    assert f.read() == 'hello'

with bz2.open(io.BytesIO(data), 'rb', compresslevel=9,
              errors='ignore') as f:
    assert f.read() == 'hello'

with bz2.open
