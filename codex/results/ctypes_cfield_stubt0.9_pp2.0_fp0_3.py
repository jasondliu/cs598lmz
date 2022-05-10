import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class P(ctypes.POINTER):
    _type_ = ctypes.c_int
    _subtype_ = ctypes.c_byte

def main():
    p1 = ctypes.pointer(ctypes.c_int(5))
    assert p1._type_ is ctypes.c_int

    p2 = ctypes.pointer(ctypes.pointer(ctypes.c_int()))
    assert p2._type_ is ctypes.POINTER
    assert p2._type_._type_ is ctypes.c_int

    p3 = ctypes.pointer(P(4))
    assert p3._type_ is P
    assert p3._type_._type_ is ctypes.c_int
    assert p3._type_._subtype_ is ctypes.c_byte

    s = ctypes.c_int()
    f1 = ctypes.c_int.from_address(ctypes.addressof(s))
    assert f1._type_ is ctypes.c_int

    f2 = ctypes.cast(ctypes.
