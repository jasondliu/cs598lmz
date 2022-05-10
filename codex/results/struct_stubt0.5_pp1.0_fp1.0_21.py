from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I', 'data')
s.pack(1)

# in Python 3.5+, you need to use a different approach
# https://docs.python.org/3.5/library/struct.html#struct.Struct.__new__
s = Struct(">I")
s.pack(1)

# in Python 3.5+, you can also use a string as the format
s = Struct(">I")
s.pack(1)
```

In the last two cases, the format string is not stored in the object.

##### Python 3.5+

`Struct` objects now support the `pack_into()` and `unpack_from()` methods.

##### Python 2.6+

`Struct` objects now support the `pack_into()` and `unpack_from()` methods.

##### Python 2.5+

`Struct` objects now support the `iter_unpack()` method.

##### Python 2.5+

`Struct` objects now support the `pack_into()` and `unpack
