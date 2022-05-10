import io
# Test io.RawIOBase
with io.RawIOBase() as f:
    pass
# Test io.BufferedIOBase
with io.BufferedIOBase() as f:
    pass
# Test io.TextIOBase
with io.TextIOBase() as f:
    pass

# Test io.BytesIO
with io.BytesIO() as f:
    pass

# Test io.StringIO
with io.StringIO() as f:
    pass

# Test io.FileIO
with io.FileIO('/dev/null') as f:
    pass

# Test io.BufferedReader
with io.BufferedReader(io.BytesIO()) as f:
    pass

# Test io.BufferedWriter
with io.BufferedWriter(io.BytesIO()) as f:
    pass

# Test io.BufferedRWPair
with io.BufferedRWPair(io.BytesIO(), io.BytesIO()) as f:
    pass

# Test io.BufferedRandom
with io.BufferedRandom(io.BytesIO()) as f:
    pass

# Test io.
