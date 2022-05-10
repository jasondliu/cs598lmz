import io
# Test io.RawIOBase.readall()

data = "A test object"
r = io.BytesIO(data)
assert r.readall() == data
assert r.readall() == b""

# Test io.RawIOBase.readall() with a timeout

# Make sure the file object has a timeout set
r.timeout = 0.5
assert r.readall() == b""

# Test io.RawIOBase.readall() with a regression in Py3.3.
# See: http://bugs.python.org/issue18117
data = "A test object"
r = io.BufferedReader(io.BytesIO(data))
assert r.readall() == data
assert r.readall() == b""
print('passed all tests...')
