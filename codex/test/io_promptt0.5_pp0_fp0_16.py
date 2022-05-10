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
