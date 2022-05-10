import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

def f(x):
    return x

def g(x):
    return ctypes.cast(x, ctypes.POINTER(S)).contents

def test_direct_call():
    result = f(ctypes.pointer(S(1, 2, 3)))
    assert result.contents.x == 1
    assert result.contents.y == 2
    assert result.contents.z == 3

def test_indirect_call():
    result = g(ctypes.pointer(S(1, 2, 3)))
    assert result.x == 1
    assert result.y == 2
    assert result.z == 3
