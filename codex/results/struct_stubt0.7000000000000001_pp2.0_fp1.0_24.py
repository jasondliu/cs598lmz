from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

s = Struct('>H')
s.size

s = Struct('>H 2s f')
s.size

s = Struct('>H 2s f')
s.pack(1, b'ab', 2.7)

s.unpack(b'\x00\x01ab\x00\x00\x00@')

s.unpack_from(b'\x00\x01ab\x00\x00\x00@\x00\x01cd\x00\x00\x00@', 2)

s.iter_unpack(b'\x00\x01ab\x00\x00\x00@\x00\x01cd\x00\x00\x00@')

s.iter_unpack(b'\x00\x01ab\x00\x00\x00@\x00\x01cd\x00\x00\x00@', 2)

s.get_size()

s.format

s
