from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('2i 3h', False)
s.size

>>> from _struct import Struct
>>> s = Struct('2i 3h')
>>> s.size
10

>>> from _struct import Struct
>>> s = Struct('2i 3h')
>>> s.format
'2i 3h'

>>> from _struct import Struct
>>> s = Struct('2i 3h')
>>> s.pack(1, 2, 3, 4, 5)
b'\x01\x00\x00\x00\x00\x00\x00\x02\x00\x03\x00\x04\x00\x05\x00'

>>> from _struct import Struct
>>> s = Struct('2i 3h')
>>> s.pack(1, 2, 3, 4, 5)
b'\x01\x00\x00\x00\x00\x00\x00\x02\x00\x03\x00\x04\x00\x05\x00'

>>> from _struct import Struct
>>> s =
