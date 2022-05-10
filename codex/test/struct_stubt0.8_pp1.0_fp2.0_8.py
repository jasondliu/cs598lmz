from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HH'
s.size = calcsize(s.format)
unpack = s.unpack

# fmt: off
SHORT_MASK    = 0x0000ffff
SHORT_LONG    =  0x10000
SHORT_OBJECT  =  0x20000
SHORT_SIZE    =  0x40000
SHORT_NODEC   =  0x80000
# fmt: on

LONG_SIZE = 0x80000000
LONG_NODEC = 0x40000000

# fmt: off
set_ = frozenset

PY3 = False

if PY3:
    def unpack_short(data, offset):
        return unpack(data[offset : offset+2])[0]
    def unpack_long(data, offset):
        return (unpack(data[offset : offset+2])[0] |
            (unpack(data[offset+2 : offset+4]) << 16))
