import io
# Test io.RawIOBase
f = io.BytesIO()
assert f.read() == b''
assert f.read() == b''
f.close()
