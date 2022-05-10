import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    x = 42

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
    x = 42
    y = 13

class U(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

def test(msg):
    print(msg, end=' ')

    test("field reordering")
    e = T()
    assert e.x == 42 and e.y == 13
    assert len(e) == 8
    e = T(1, 2)
    assert e.x == 1 and e.y == 2

    test("__slots__")
    assert "x" not in dir(S())
    try:
        S().x
    except AttributeError:
        pass

    test("no_init")
    e = U()
    try:
        e.x
    except AttributeError:
        pass
   
