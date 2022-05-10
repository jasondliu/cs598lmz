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
</code>
At the end of every loop through all possible partial reads of <code>s</code> we print <code>-</code> and a carriage return, so we can watch the progress of the program. This works in both Python 2 (<code>print</code> has a <code>end='\r'
