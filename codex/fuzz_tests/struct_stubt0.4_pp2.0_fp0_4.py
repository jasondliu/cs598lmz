from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = Struct.calcsize(s, s.format)

def pack(i):
    return s.pack(i)

def unpack(b):
    return s.unpack(b)[0]

def test_pack_unpack():
    for i in range(1, 10):
        b = pack(i)
        assert unpack(b) == i

def test_pack_unpack_large():
    for i in range(1, 10):
        b = pack(2**(i*8))
        assert unpack(b) == 2**(i*8)
