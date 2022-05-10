import io
# Test io.RawIOBase
with io.RawIOBase() as r:
    print(r.read(1))

# Test io.BufferedIOBase
with io.BufferedIOBase() as b:
    print(b.read(1))

# Test io.TextIOBase
with io.TextIOBase() as t:
    print(t.read(1))

# Test io.StringIO
with io.StringIO() as s:
    print(s.read(1))

# Test io.BytesIO
with io.BytesIO() as b:
    print(b.read(1))

# Test io.FileIO
with io.FileIO("test.txt", "r") as f:
    print(f.read(1))

# Test io.TextIOWrapper
with io.TextIOWrapper(io.BytesIO()) as t:
    print(t.read(1))

# Test io.BufferedReader
with io.BufferedReader(io.BytesIO()) as b:
    print(b.read(1))

# Test io.Buff
