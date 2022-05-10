from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()

# unpack
print(s.unpack(data))
# (1, b'ab', 2.7000000)

# unpack_from
print(s.unpack_from(data, 4))
# (1, b'ab', 2.7000000)
```

--------------------------------------------------------------------------------

## [7.5. _struct — Interpret bytes as packed binary data](https://docs.python.org/3/library/_struct.html#module-_struct)

### [7.5.1. Struct objects](https://docs.python.org/3/library/_struct.html#struct-objects)

#### [7.5.1.1. class struct.Struct([format])](https://docs.python.org/3/library/_struct.html#struct.Struct)

```py
class struct.Struct([format])
```

Return a new Struct object which writes and reads binary data according to the format string format.

The format string is composed of one or more of the basic
