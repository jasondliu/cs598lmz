import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_ctypes_callback():
    def callback(x):
        return x + 42

    cb = FUNTYPE(callback)
    assert cb(6) == 48
    cb = FUNTYPE(lambda x: x + 42)
    assert cb(6) == 48

def test_get_ctypes_function_type():
    from _ctypes import get_ctypes_function_type
    assert get_ctypes_function_type(lambda x: x + 6) is FUNTYPE
    def f(x):
        return x + 6
    assert get_ctypes_function_type(f) is FUNTYPE
    raises(TypeError, get_ctypes_function_type, 42)

def test_ctypes_functions_returning_void():
    from _ctypes import FUNCFLAG_CDECL
    from _rawffi import size_alignment
    from _rawffi import FuncPtr
    from _ctypes import get_ctypes_function_type
    import _libc
    cb = FUNTYPE(lambda x:
