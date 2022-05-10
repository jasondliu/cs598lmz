import io
# Test io.RawIOBase

# Test the RawIOBase constructor
io.RawIOBase()

# Test the RawIOBase read() method
r = io.RawIOBase()
r.read(10)

# Test the RawIOBase write() method
w = io.RawIOBase()
w.write(b"hello world")

# Test the RawIOBase seek() method
s = io.RawIOBase()
s.seek(10, 0)
s.seek(10, 1)
s.seek(10, 2)

# Test the RawIOBase tell() method
t = io.RawIOBase()
t.tell()

# Test the RawIOBase readinto() method
ri = io.RawIOBase()
ri.readinto(bytearray(10))

# Test the RawIOBase readall() method
ra = io.RawIOBase()
ra.readall()

# Test the RawIOBase close() method
c = io.RawIOBase()
c.close()

# Test the RawIOBase fileno() method
f = io.RawIOBase()
f.
