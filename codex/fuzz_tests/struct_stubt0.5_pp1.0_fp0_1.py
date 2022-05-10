from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(">I")
s.pack(0x12345678)
```

```
>>> import _struct
>>> s = _struct.Struct.__new__(_struct.Struct)
>>> s.__init__(">I")
>>> s.pack(0x12345678)
b'xV4\x12'
```

```
>>> import _struct
>>> s = _struct.Struct.__new__(_struct.Struct)
>>> s.__init__(">I")
>>> s.pack(0x12345678)
b'xV4\x12'
```

```
>>> import _struct
>>> s = _struct.Struct.__new__(_struct.Struct)
>>> s.__init__(">I")
>>> s.pack(0x12345678)
b'xV4\x12'
```

```
>>> import _struct
>>> s = _struct.Struct.__new__(_struct.Struct)
>>> s.__init__(">I")
>>> s.pack(0x
