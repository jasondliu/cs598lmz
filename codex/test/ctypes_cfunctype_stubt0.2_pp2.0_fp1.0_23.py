import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_cfuntype():
    assert fun() == 42

def test_cfuntype_exception():
    def f():
        raise ValueError
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    f1 = FUNTYPE(f)
    raises(ValueError, f1, 1)

def test_cfuntype_exception_2():
    def f():
        raise ValueError
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    f1 = FUNTYPE(f)
    raises(ValueError, f1, 1)

def test_cfuntype_exception_3():
    def f():
        raise ValueError
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    f1 = FUNTYPE(f)
    raises(ValueError, f1, 1)

