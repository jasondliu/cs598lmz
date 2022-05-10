import io
# Test io.RawIOBase
f = io.BytesIO()
f.write(b"hello world")
f.seek(0)
print(f.read())

# Test io.BufferedIOBase
f = io.BytesIO()
b = io.BufferedWriter(f)
b.write(b"hello world")
b.seek(0)
print(b.read())

# Test io.TextIOBase
f = io.StringIO()
f.write("hello world")
f.seek(0)
print(f.read())

# Test io.FileIO
with io.FileIO("/tmp/foo", "w") as f:
    f.write(b"hello world")
with io.FileIO("/tmp/foo", "r") as f:
    print(f.read())

# Test io.FileIO
with io.FileIO("/tmp/foo", "w") as f:
    b = io.BufferedWriter(f)
    b.write(b"hello world")
with io.FileIO("/tmp/foo", "r") as f:

