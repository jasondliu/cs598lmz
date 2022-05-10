import io
# Test io.RawIOBase.
r = io.RawIOBase()
r.read()
r.read(10)
r.read1()
r.readinto(bytearray(10))
r.readinto1(bytearray(10))
# Test io.BufferedIOBase.
r = io.BufferedIOBase()
r.read()
r.read(10)
r.read1()
r.readinto(bytearray(10))
r.readinto1(bytearray(10))
s = io.BufferedRandom(r)
s.write(bytearray(10))
s.write( memoryview(bytearray(10)))
# Test io.BytesIO.
s = io.BytesIO()
s.close()
s.flush()
s.getvalue()
s.isatty()
s.peek()
s.seek(10)
s.seek(-10, 2)
s.tell()
s.truncate(10)
s.truncate()
# Test io.StringIO.
s = io.StringIO
