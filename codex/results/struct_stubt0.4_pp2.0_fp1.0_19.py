from _struct import Struct
s = Struct.__new__(Struct)

s.__init__('I 2s f')
s.size

s.pack(1, 'ab'.encode('utf-8'), 2.7)

# _asdict()
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

s = Stock('ACME', 100, 123.45)
s

s._asdict()

# _replace()
s = s._replace(shares=75)
s

# _fields
s._fields

# _make()
Stock._make(['ACME', 100, 123.45])

# _source
Stock.__doc__

Stock.__source__

# _field_defaults
Stock._field_defaults

# _field_types
Stock._field_types

# _field_defaults
Stock._field_defaults
