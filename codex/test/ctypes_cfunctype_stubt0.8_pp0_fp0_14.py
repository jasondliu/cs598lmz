import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

@FUNTYPE
def fun2(foo):
    return foo

assert fun() is None
assert fun2(42) == 42
try:
    import _codecs
except ImportError:
    pass
else:
    class Foo(ctypes.Structure):
        _fields_ = [('bar', ctypes.c_int)]
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.POINTER(Foo))
    @FUNTYPE
    def fun():
        return _codecs.escape_encode(b'foo')[0]

    assert fun().decode('ascii') == 'foo'
    assert fun().decode('ascii') == 'foo'

