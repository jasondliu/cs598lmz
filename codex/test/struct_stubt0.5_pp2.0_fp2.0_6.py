from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

def test_struct_pack(buf):
    return s.pack(buf)

def test_struct_unpack(buf):
    return s.unpack(buf)[0]

def test_struct_unpack_from(buf):
    return s.unpack_from(buf, 0)[0]

def test_struct_iter_unpack(buf):
    return next(s.iter_unpack(buf))

def test_struct_iter_unpack_from(buf):
    return next(s.iter_unpack_from(buf, 0))

def test_struct_calcsize(buf):
    return s.calcsize(buf)

def test_struct_pack_into(buf):
    return s.pack_into(buf, 0, 0)

def test_struct_unpack_from(buf):
    return s.unpack_from(buf, 0)
