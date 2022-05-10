from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('__doc__', '''Compiled struct pattern.

Used to create compiled struct objects which can be used as follows:

    >>> from _struct import Struct
    >>> st = Struct('i?f')
    >>> s = st.pack(1, 0, 2.5)
    >>> st.unpack(s)
    (1, False, 2.5)

For more information regarding the struct standard see
https://docs.python.org/library/struct.html
''')
s.__setattr__('__init__', lambda self, fmt:
    self.format = fmt)
s.__setattr__('pack', lambda self, *args:
    bytearray(struct.Struct(self.format).pack(*args)))
s.__setattr__('unpack', lambda self, data:
    struct.Struct(self.format).unpack(data))
s.__setattr__('unpack_from', lambda self, data, off = 0:
    struct.Struct(self.format).unpack_from(data, off))
s.__set
