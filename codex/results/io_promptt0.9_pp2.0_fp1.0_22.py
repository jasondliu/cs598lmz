import io
# Test io.RawIOBase and io.BufferedIOBase

i = io.BytesIO(b'abc')

assert type(i) is io.BytesIO
assert not isinstance(i, io.RawIOBase)
assert isinstance(i, io.BufferedIOBase)
i = io.StringIO('abc')

assert type(i) is io.StringIO
assert not isinstance(i, io.RawIOBase)
assert isinstance(i, io.BufferedIOBase)
# Test io.RawIOBase and io.BufferedIOBase

i = io.FileIO('test.file')

assert type(i) is io.FileIO
assert isinstance(i, io.RawIOBase)
assert isinstance(i, io.BufferedIOBase)
 
# Note that BytesIO and StringIO implement an additional non-stream interface
# that depends on their __init__ argument.

 
# When using a raw file, the type depends on the mode.  On Windows, text
# mode is implied, so text and binary mode files have different types.
if os.name == 'nt': 
