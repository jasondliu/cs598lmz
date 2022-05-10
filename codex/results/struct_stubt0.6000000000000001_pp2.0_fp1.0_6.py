from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<3sf')
s.unpack(b'\x00\x00\x00\x00\x00\x00\x08@')

s = Struct('<3sf')
s.unpack(b'\x00\x00\x00\x00\x00\x00\x08@')

s = Struct.__new__(Struct)
s.__init__('<3sf')
s.unpack_from(b'\x00\x00\x00\x00\x00\x00\x08@', 0)

s = Struct('<3sf')
s.unpack_from(b'\x00\x00\x00\x00\x00\x00\x08@', 0)

s = Struct.__new__(Struct)
s.__init__('<3sf')
s.pack(0, 0.0)

s = Struct('<3sf')
s.pack(0, 0.0)

s = Struct.__new__(Struct)
s
