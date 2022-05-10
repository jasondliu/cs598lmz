from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# pack
>>> s.pack(1, b'ab', 2.7)
b'\x01ab\x00\x00\x00\x00\x00\x00\xcd\xcc\x8c\x3f'

# unpack
>>> s.unpack(b'\x01ab\x00\x00\x00\x00\x00\x00\xcd\xcc\x8c\x3f')
(1, b'ab', 2.6999998092651367)

# calcsize
>>> s.calcsize()
12
```

## 4.2.3.2.2. `array`

```python
from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)

# array('H', [4000, 10, 700, 22222])
a[1:3]

# array('H', [10, 700])
```

## 4.
