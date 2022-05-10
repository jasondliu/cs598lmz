from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# prints:
# b'\x01\x00\x00\x00'
```

```py
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# prints:
# (1,)
```

```py
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.iter_unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00')

# prints:
# <iterator object at 0x7f9f6b9d9e48>
```

## License

MIT
