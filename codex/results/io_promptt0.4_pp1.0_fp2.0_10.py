import io
# Test io.RawIOBase
with io.BytesIO() as f:
    f.read()
# Test io.BufferedIOBase
with io.BytesIO() as f:
    f.read()
# Test io.TextIOBase
with io.StringIO() as f:
    f.read()
# Test io.FileIO
with io.FileIO('/dev/null', 'r') as f:
    f.read()
# Test io.BufferedWriter
with io.BytesIO() as f:
    with io.BufferedWriter(f) as bf:
        bf.write(b'foo')
# Test io.BufferedReader
with io.BytesIO() as f:
    f.write(b'foo')
    f.seek(0)
    with io.BufferedReader(f) as bf:
        bf.read()
# Test io.BufferedRandom
with io.BytesIO() as f:
    with io.BufferedRandom(f) as bf:
        bf.write(b'foo')
        bf.seek(0)
        bf
