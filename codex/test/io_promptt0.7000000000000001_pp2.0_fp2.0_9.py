import io
# Test io.RawIOBase
with io.BytesIO() as f:
    print(f.read())

# Test io.BufferedIOBase
with io.StringIO() as f:
    print(f.read())
