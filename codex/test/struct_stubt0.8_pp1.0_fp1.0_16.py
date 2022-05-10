from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(
    format='>HH',
    size=4
)
s.unpack(b'\x00\x01\x00\x02')
# (1, 2)
