import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_fp_byval_struct_arg():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]
    def f(s):
        return s.x
    assert f(S(42)) == 42

def test_fp_byval_struct_return():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]
    def f():
        s = S(42)
        return s.x
    assert f() == 42

def test_fp_byval_struct_residual_call():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]
    def f():
        s = S(42)
        return S.x.__get__(s)
    assert f() == 42

def test_fp_byval_struct_residual_call_ctypes():
    class S(ctypes.Structure):
        _fields_ = [('x',
