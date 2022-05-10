import _struct
# Test _struct.Struct with a non-native format
s = _struct.Struct('<I')
# This works
s.pack(1)
# This doesn't
s.pack(1, 2)
```

```
Traceback (most recent call last):
  File "test.py", line 6, in <module>
    s.pack(1, 2)
TypeError: pack expected exactly 1 arguments, got 2
```

### _struct.Struct.unpack_from(buffer, offset=0)

```
>>> import _struct
>>> s = _struct.Struct('<I')
>>> s.unpack_from(b'\x00\x00\x00\x01')
(1,)
>>> s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x02')
(1,)
>>> s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x02', offset=4)
(2,)
```


