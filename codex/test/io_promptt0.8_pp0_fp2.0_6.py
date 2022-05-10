import io
# Test io.RawIOBase
f = io.StringIO("some data")
f.readable()

# Test io.IOBase
f = io.StringIO("some data")
f.writable()

# Test io.TextIOBase
f = io.StringIO("some data")
f.writable()

# Test io.BufferedIOBase
f = io.BytesIO(b"some data")
f.readable()

# Test io.FileIO

