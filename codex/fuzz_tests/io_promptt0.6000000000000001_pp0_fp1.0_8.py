import io
# Test io.RawIOBase
with io.RawIOBase() as f:
    f.read()
# Test io.BufferedIOBase
with io.BufferedIOBase() as f:
    f.read()
# Test io.TextIOBase
with io.TextIOBase() as f:
    f.read()
# Test io.FileIO
with io.FileIO("/dev/null") as f:
    f.read()
# Test io.BytesIO
with io.BytesIO() as f:
    f.write(b"")
# Test io.StringIO
with io.StringIO() as f:
    f.write("")
# Test io.BufferedReader
with io.BufferedReader(io.BytesIO()) as f:
    f.read()
# Test io.BufferedWriter
with io.BufferedWriter(io.BytesIO()) as f:
    f.write(b"")
# Test io.BufferedRWPair
with io.BufferedRWPair(io.BytesIO(), io.BytesIO()) as f:
    f.read()
# Test io.Buff
