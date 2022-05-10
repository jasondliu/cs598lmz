import io
# Test io.RawIOBase
with io.BytesIO() as b:
    assert isinstance(b, io.RawIOBase)
# Test io.BufferedIOBase
with io.BytesIO() as b:
    assert isinstance(b, io.BufferedIOBase)
# Test io.TextIOBase
with io.StringIO() as b:
    assert isinstance(b, io.TextIOBase)

# Test io.FileIO
with io.FileIO('README.md', 'r') as f:
    assert isinstance(f, io.RawIOBase)

# Test io.BufferedRandom
with io.BytesIO() as b:
    assert isinstance(b, io.BufferedRandom)

# Test io.BufferedWriter
with io.BytesIO() as b:
    assert isinstance(b, io.BufferedWriter)

# Test io.BufferedRWPair
with io.BytesIO() as b:
    assert isinstance(b, io.BufferedRWPair)

# Test io.BufferedReader
with io.BytesIO() as b:
    assert
