import io
# Test io.RawIOBase
with io.RawIOBase() as f:
    print(type(f))

# Test io.BufferedIOBase
with io.BufferedIOBase() as f:
    print(type(f))

# Test io.TextIOBase
with io.TextIOBase() as f:
    print(type(f))

# Test io.BytesIO
with io.BytesIO() as b:
    print(type(b))

# Test io.StringIO
with io.StringIO() as s:
    print(type(s))

# Test io.FileIO
with io.FileIO('foo.txt', 'w') as f:
    print(type(f))

# Test io.BytesIO.getvalue
b = io.BytesIO(b"some initial binary data: \x00\x01")
print(b.getvalue())

# Test io.StringIO.getvalue
s = io.StringIO("some initial text data")
print(s.getvalue())

# Test io.TextIOWrapper.detach
