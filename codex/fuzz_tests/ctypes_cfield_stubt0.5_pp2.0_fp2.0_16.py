import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_type():
    print(S.x.__class__)
    print(type(S.x))
    print(ctypes.CField)
    assert type(S.x) is ctypes.CField

def test_cfield_name():
    print(S.x.name)
    assert S.x.name == 'x'

def test_cfield_type_name():
    print(S.x.type_name)
    assert S.x.type_name == 'int'

def test_cfield_offset():
    print(S.x.offset)
    assert S.x.offset == 0

def test_cfield_size():
    print(S.x.size)
    assert S.x.size == 4

def test_cfield_bitsize():
    print(S.x.bitsize)
    assert S.x.bitsize == 32

def test_cfield_ctypes_type():
    print(S.x.ctypes_type)
    assert S.x.ctypes
