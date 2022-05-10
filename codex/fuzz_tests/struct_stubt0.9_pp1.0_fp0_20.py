from _struct import Struct
s = Struct.__new__(Struct)
<Buffer 00 00 00 00 00 00>
>>> s.__sizeof__()
7
>>> s.size
7
>>> s
Struct('=')
>>> s.format
'='
>>> s.unpack(b'/tmp/download')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: buffer is too short for a 7 byte long
>>> s.pack(s.unpack(b'\x00\x00\x00\x00\x00\x00')) == b'\x00\x00\x00\x00\x00\x00'
True
>>> s.size
7
>>> s
Struct('=')
>>> 'Struct(\''+s.format+'\', '+repr(s.size)+')'
"Struct('=', 7)"
```

```Python
>>> from _struct import Struct
s = Struct(0)
<Buffer 00 00 00 00 00 00>
>>> s.__sizeof__()
7
>>> s.size
7
>>> s

