from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl', 'little')
print(type(s))
print(s.size)
print(list(map(hex, s.unpack(b'\x01\x02\x03\x04\x05\x06'))))
