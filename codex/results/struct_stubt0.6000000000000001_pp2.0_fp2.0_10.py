from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', [])
s.unpack(b'\x00\x00\x00\x00')
```

```
>>> from _struct import Struct
>>> import ctypes
>>> s = Struct.__new__(Struct)
>>> s.__init__('i', [])
>>> ctypes.string_at(s.unpack(b'\x00\x00\x00\x00'), 4)
b'\x00\x00\x00\x00'
>>> ctypes.string_at(s.unpack(b'\x00\x00\x00\x00'), 4)
b'\x00\x00\x00\x00'
>>> ctypes.string_at(s.unpack(b'\x00\x00\x00\x00'), 4)
b'\x00\x00\x00\x00'
>>> ctypes.string_at(s.unpack(b'\x00\x00\x00\x00'), 4)
b'\x00\x
