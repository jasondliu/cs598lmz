from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__['format'] = 'I H'
s.__dict__['size'] = s.size
print(s.size)
print(s.format)
print(s.unpack_from(b'\x00\x00\x00\x08\x00\x00', 4))
# => (524288, 0)

print(s.unpack_from(b'\x00\x00\x00\x08\x00\x00'))
# => (8, 0)
```

```
$ python3.6 0.py
8
I H
(524288, 0)
```

#### 3.4.4.5.4.5.5.5.5.5.5.5.5.5.5.5.5.5.5.5.5.5.5.5.5.5.5

#### 3.4.4.5.4.5.5.5.5.5.5.5.5.5.5.5.5.5.5.5.5
