import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 2
@FUNTYPE
def fail():
    raise RuntimeError

def test_varargs_call():
    C = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    a = ctypes.c_int(2)
    assert C(a) == 2

def test_fun():
    assert fun() == 2
    raises(RuntimeError, fail)

    TYPE = ctypes.CFUNCTYPE(ctypes.py_object,
                            ctypes.c_int, ctypes.py_object)
    args = (1, "hello")
    assert TYPE(fun)(*args) == 2
    raises(RuntimeError, TYPE(fail), *args)

def test_misc():
    import ctypes.util
    def check(name, argtypes, restype):
        func = ctypes.cdll.msvcrt[name]
        assert func.argtypes[:-1] == argtypes
        assert func.restype == restype
        func.argtypes = argtypes
        assert func.argtypes
