import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function_with_kwargs():
    def f(a, b, c):
        return a, b, c
    assert call_function(f, 1, 2, 3) == (1, 2, 3)
    assert call_function(f, 1, 2, 3, a=4, b=5, c=6) == (4, 5, 6)
    assert call_function(f, 1, 2, 3, a=4, b=5, c=6, d=7) == (4, 5, 6)
    assert call_function(f, 1, 2, 3, a=4, b=5, c=6, d=7, e=8) == (4, 5, 6)
    assert call_function(f, 1, 2, 3, a=4, b=5, c=6, d=7, e=8, f=9) == (4, 5, 6)
