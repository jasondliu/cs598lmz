from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl')

s.pack(1, 2, 3)

s.unpack(b'\x00\x01\x00\x02\x00\x00\x00\x03')

s.pack_into(b'\x00'*12, 4, 1, 2, 3)

s.unpack_from(b'\x00'*4 + b'\x00\x01\x00\x02\x00\x00\x00\x03')

# _struct.Struct is a class, so it can be subclassed.

class Struct(Struct):
    def __init__(self, format, endianness='='):
        super().__init__(endianness + format)
        self.endianness = endianness

s = Struct('hhl', '<')
s.pack(1, 2, 3)

# The Struct class can be used as a function to create new Struct
# instances.

Struct('hhl')

# The new Struct instances are callable.

