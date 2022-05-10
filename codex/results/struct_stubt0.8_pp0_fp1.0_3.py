from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.pack(2039)

with open('unpacked.bin', 'rb') as file:
    data = file.read()

assert s.unpack(data) == (2039,)
