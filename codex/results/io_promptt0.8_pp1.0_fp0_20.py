import io
# Test io.RawIOBase
io.RawIOBase()
# Test io.BufferedIOBase
io.BufferedIOBase()
# Test io.TextIOBase
io.TextIOBase()

# Test io.BytesIO
io.BytesIO
io.BytesIO(b"raw data")
io.BytesIO(u"raw uni data")

# Test io.StringIO
io.StringIO
io.StringIO(u"raw uni data")

# Test io.BufferedReader
io.BufferedReader(io.BytesIO(b"abcdefg"))

# Test io.BufferedWriter
io.BufferedWriter(io.BytesIO())

# Test io.BufferedRWPair
io.BufferedRWPair(io.BytesIO(b"abcdefg"), io.BytesIO(b"hijklmnop"))

# Test io.BufferedRandom
io.BufferedRandom(io.BytesIO(b"abcdefg"))

# Test io.FileIO
io.FileIO
io.FileIO("test_io_file")
io.FileIO("test_io
