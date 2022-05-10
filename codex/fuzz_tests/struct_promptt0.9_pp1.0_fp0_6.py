import _struct
# Test _struct.Struct
>>> s = _struct.Struct(b'hhl')
>>> s.size
8
>>> s.pack(1, 2, 3)
b'\x01\x00\x02\x00\x03\x00\x00\x00'
>>> s.unpack(b'\x01\x00\x02\x00\x03\x00\x00\x00')
(1, 2, 3)
>>> s.unpack(b'x') # Wrong size raises a StructError
Traceback (most recent call last):
 ...
_struct.error: unpack requires a buffer of 8 bytes
>>> for c in [b'b', b'B', b'h', b'H', b'i', b'I', b'l', b'L', b'q', b'Q',
... b'f', b'd']:
...     s = _struct.Struct(c)
...     assert s.size == struct.calcsize(c)
...     assert s.pack(1) == struct.pack(c, 1)
...
>>> # Non
