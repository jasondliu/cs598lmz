from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = Struct.calcsize(s.format)

def iter_unpack(data):
    count = len(data) // s.size
    for i in range(count):
        yield s.unpack_from(data, i*s.size)

def iter_pack(data):
    for i in data:
        yield s.pack(*i)

def unpack(data):
    return list(iter_unpack(data))

def pack(data):
    return b''.join(iter_pack(data))

def test_unpack():
    data = b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
    assert unpack(data) == [(1,), (2,), (3,)]

def test_pack():
    data = [(1,), (2,), (3,)]
