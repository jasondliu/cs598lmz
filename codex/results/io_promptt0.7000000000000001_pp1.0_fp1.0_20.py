import io
# Test io.RawIOBase
f = io.RawIOBase()
f.readline()
# Test io.BufferedIOBase
f = io.BufferedIOBase()
f.read()
# Test io.BytesIO
f = io.BytesIO()
f.read()
# Test io.StringIO
f = io.StringIO()
f.readline()
# Test io.TextIOBase
f = io.TextIOBase()
f.read()
# Test io.TextIOWrapper
f = io.TextIOWrapper(io.BytesIO())
f.read()
# Test io.FileIO
f = io.FileIO()
f.read()
# Test io.FileIO
f = io.FileIO(tempfile.mkstemp()[1], 'rb')
f.read()
# Test io.FileIO
f = io.FileIO(tempfile.mkstemp()[1], 'wb')
f.read()
# Test io.BufferedReader
f = io.BufferedReader(open(tempfile.mkstemp()[1]))
f.read()

