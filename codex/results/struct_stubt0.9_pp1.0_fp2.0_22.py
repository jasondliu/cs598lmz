from _struct import Struct
s = Struct.__new__(Struct)
s.endian = '<'
s.format = 'H3s'

row = (2015, b'\x13\x12\x15')

# py2: bytearray returned
buffer(s.pack(*row))

# py3: bytes returned
s.pack(*row)

# buffer(s.pack() not supported and returns
# TypeError: buffer is not callable
