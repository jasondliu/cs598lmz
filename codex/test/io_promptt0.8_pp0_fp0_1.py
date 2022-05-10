import io
# Test io.RawIOBase
file = io.FileIO("foo.txt")

# Test io.BufferedIOBase
buffer = io.BufferedReader(file)

# Test io.TextIOBase
text = io.TextIOWrapper(buffer)
text.read()

# Test io.BytesIO
bytes = io.BytesIO()
bytes.getvalue()

# Test io.StringIO
io.StringIO()

# Test io.BytesIO
io.BytesIO()

# Test io.BufferedReader(bytes)
io.BufferedReader(io.BytesIO())

# Test io.BufferedWriter(bytes)
io.BufferedWriter(io.BytesIO())
