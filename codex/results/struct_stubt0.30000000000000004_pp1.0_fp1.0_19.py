from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2s2s'
s.size = s.calcsize(s.format)

def unpack(data):
    return s.unpack(data)

def pack(data):
    return s.pack(*data)

def test():
    assert unpack(pack((b'\x00\x00', b'\x00\x00'))) == (b'\x00\x00', b'\x00\x00')
    assert unpack(pack((b'\x00\x01', b'\x00\x00'))) == (b'\x00\x01', b'\x00\x00')
    assert unpack(pack((b'\x00\x00', b'\x00\x01'))) == (b'\x00\x00', b'\x00\x01')
    assert unpack(pack((b'\x00\x01', b'\x00\x01'))) == (b'\x00\x01', b'\x00\x01')

