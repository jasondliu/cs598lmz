import io
# Test io.RawIOBase (raw I/O), .readinto()

# Test direct calls

io.ByteIO(b"abc")
io.BytesIO(b"abc")
io.StringIO("abc")
io.BufferedReader(io.BytesIO(b"abc"))
io.BufferedWriter(io.BytesIO(b"abc"))
i
