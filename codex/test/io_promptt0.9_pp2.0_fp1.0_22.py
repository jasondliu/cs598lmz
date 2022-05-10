import io
# Test io.RawIOBase and io.BufferedIOBase

i = io.BytesIO(b'abc')

assert type(i) is io.BytesIO
assert not isinstance(i, io.RawIOBase)
assert isinstance(i, io.BufferedIOBase)
i = io.StringIO('abc')

assert type(i) is io.StringIO
assert not isinstance(i, io.RawIOBase)
