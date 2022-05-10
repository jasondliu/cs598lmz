from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

c = s.pack(23, False, 42.0)
c
c[1] = '\x01'

s.unpack(c)

s = Struct('i?f')
s.pack(23, False, 42.0)
s.pack(23, True, 42.0)
# ValueError: 20 is not one of (1, 2, 4, 8)
s.pack(23, 1, 42.0)

s = Struct('i?f')
s.pack(23, False, 42.0)
s.pack(b'N/A', False, 42.0)
# struct.error: argument for 's' must be a bytes object of length 2
s.pack(b'NA', False, 42.0)

s = Struct('i?f')
s.pack(23, False, 42.0)
# struct.error: argument for 'c' must be a single character
s.pack(23, 'xy', 42.0)

s = Struct('i
