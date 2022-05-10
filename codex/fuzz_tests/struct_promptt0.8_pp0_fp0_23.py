import _struct
# Test _struct.Struct

"""
>>> s = _struct.Struct('i')
>>> s.format
'i'
>>> s.size
4
>>> s.pack(123456)
'\x00\x01\xe2@'
>>> s.unpack('\x00\x01\xe2@')
(123456,)
>>> s.unpack_from('\x00\x01\xe2@\x00\x00\x00\x00', 0)
(123456,)
>>> s.unpack_from('\x00\x01\xe2@\x00\x00\x00\x00', 4)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
struct.error: unpack_from requires a buffer of at least 4 bytes
>>> s.pack_into('\x00\x00\x00\x00', 0, 123456)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: buffer is read-only
>>> s.pack_into(_array.
