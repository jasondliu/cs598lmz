import io
# Test io.RawIOBase by using a raw string
s = io.BytesIO(b'abc')
s.read()
# io.RawIOBase.read() calls io.RawIOBase.readinto()
s.readinto(bytearray(10))
# Test io.RawIOBase by using a bytearray
b = bytearray(b'abc')
s = io.BytesIO(b)
s.read()
# Test io.RawIOBase by using an array.array
a = array.array('B', b'abc')
s = io.BytesIO(a)
s.read()
# Test io.RawIOBase by using a memoryview
m = memoryview(b'abc')
s = io.BytesIO(m)
s.read()
 
# Test io.RawIOBase by using a C array
import ctypes
ca = (ctypes.c_uint8 * len(m))(*m)
s = io.BytesIO(ca)
s.read()
s = io.StringIO('abc')
s.read(10)
# Test io.RawIOBase
