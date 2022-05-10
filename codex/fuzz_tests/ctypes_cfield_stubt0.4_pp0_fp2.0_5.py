import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int),
                ('z', ctypes.c_int)]

ctypes.CStructure = type(C)

class D(C):
    _fields_ = [('u', ctypes.c_int),
                ('v', ctypes.c_int)]

ctypes.CUnion = type(ctypes.Union)

def test_type_equality():
    assert type(ctypes.c_char_p) is ctypes.CStringType
    assert type(ctypes.c_wchar_p) is ctypes.CStringType
    assert type(ctypes.c_char_p) is not ctypes.CUnicodeType
    assert type(ctypes.c_wchar_p) is not ctypes.CUnicodeType
    assert type(ctypes.c_char_p) is not ctypes.CArrayType
    assert type(ctypes.c_wchar_p) is not ctypes.CArrayType
    assert type(
