from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i9sh'
s.size = s.calcsize(s.format)

for part in (
    b'0123456789', b'01234567890', b'012345678901', b'0123456789012', b'01234567890123',
    b'012345678901234', b'0123456789012345', b'01234567890123456', b'012345678901234567',
    ):
    print(repr(s.unpack(part)))
    print(repr(s.unpack(part + b'8')))
    print(repr(s.unpack(part + b'p')))
    print('-')
