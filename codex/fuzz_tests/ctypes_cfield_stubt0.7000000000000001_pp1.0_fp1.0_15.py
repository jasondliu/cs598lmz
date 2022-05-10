import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    it = iter(S.x)
    assert next(it) == None
    assert next(it) == 'x'
    assert next(it) == ctypes.c_int
    raises(StopIteration, next, it)

def test_cfield_name():
    assert S.x.name == 'x'

def test_cfield_offset():
    assert S.x.offset == ctypes.sizeof(ctypes.c_int)

def test_cfield_size():
    assert S.x.size == ctypes.sizeof(ctypes.c_int)

def test_cfield_ctype():
    assert S.x.ctype == ctypes.c_int

def test_cfield_pack_unpack():
    assert S.x.pack(1) == (1).to_bytes(ctypes.sizeof(ctypes.c_int), 'little')
    assert S.x.unpack((1).to_bytes(ctypes.sizeof(ctypes.c_int), '
