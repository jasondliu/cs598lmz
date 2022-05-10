import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1,2,3)

def test_bad_retval():
    x = fun()
    assert x == (1,2,3)
    raises(ctypes.ArgumentError, "list(fun())")

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_int),
                ]

def test_struct_retval():
    FUNTYPE2 = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.c_int, ctypes.c_int)
    @FUNTYPE2
    def foo(a, b):
        return X(a, b, 0, 0, 0)
    assert foo(1, 2) == (1, 2, 0, 0, 0)
    assert list(foo(1, 2)) == [1, 2, 0, 0, 0]



