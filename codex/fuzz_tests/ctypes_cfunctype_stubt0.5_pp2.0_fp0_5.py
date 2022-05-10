import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_cfuntype():
    assert fun() == 42

def test_cfuntype_callable():
    class C:
        f = fun
    assert C().f() == 42

class CFuncPtr(ctypes.CFUNCTYPE):
    _argtypes_ = ctypes.c_int, ctypes.c_double
    _restype_ = ctypes.c_double

@CFuncPtr
def fun2(x, y):
    return x + y

def test_cfuncptr():
    assert fun2(2, 3.5) == 5.5

def test_cfuncptr_callable():
    class C:
        f = fun2
    assert C().f(2, 3.5) == 5.5

def test_cfuncptr_callable_with_args():
    class C:
        f = fun2
    assert C().f(2, y=3.5) == 5.5

def test_cfuncptr_callable_with_kwargs():
    class C:
       
