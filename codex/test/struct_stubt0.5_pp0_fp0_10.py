from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H', 'foo')
s.unpack(b'\x01\x00')

# extra bytes should be ignored
s.unpack(b'\x01\x00\x00\x00')

# endianness should be ignored
s.unpack(b'\x00\x01')

# size should be ignored
s.unpack(b'\x00\x00\x00')

# size should be ignored
s.unpack(b'\x00\x00\x00\x00')

# invalid size
s.unpack(b'\x00\x00\x00\x00\x00')

# invalid size
s.unpack(b'\x00\x00\x00\x00\x00\x00')

# invalid size
s.unpack(b'\x00\x00\x00\x00\x00\x00\x00')

# invalid size
