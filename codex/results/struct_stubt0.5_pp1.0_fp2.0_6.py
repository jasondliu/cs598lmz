from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>h')
s.unpack_from(b'\x00\x01', 0)
(1,)
>>> s.unpack_from(b'\x00\x01', 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
error: unpack requires a buffer of 2 bytes
```

```
>>> import _struct
>>> s = _struct.Struct('>h')
>>> s.unpack_from(b'\x00\x01', 0)
(1,)
>>> s.unpack_from(b'\x00\x01', 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
error: unpack requires a buffer of 2 bytes
```

```
>>> from struct import Struct
>>> s = Struct('>h')
>>> s.unpack_from(b'\x00\x01', 0)
(1,)
>>> s.unpack_from(b'\x00\x
