import io
# Test io.RawIOBase.readall

# Try to readall on a normal file, should just read the entire contents.
print('TEST 1:')
f = io.BytesIO(b'abc\x00d\xe5\xf6\x00ghi\x00j')
