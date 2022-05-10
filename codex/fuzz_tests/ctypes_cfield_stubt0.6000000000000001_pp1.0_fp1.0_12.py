import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('p', ctypes.c_char_p)]

def test(typ):
    x = typ()
    print(x, x.value)
    x.value = 42
    print(x, x.value)
    x.value = None
    print(x, x.value)
    x.value = b'\x42'
    print(x, x.value)
    x.value = b'x'
    print(x, x.value)

    x = typ(42)
    print(x, x.value)
    x = typ(None)
    print(x, x.value)
    x = typ(b'\x42')
    print(x, x.value)
    x = typ(b'x')
    print(x, x.value)

def test_cfield(typ):
    x = typ()
    print(x, x.value)
    x.value = 42
    print(x, x.value)
    x.value
