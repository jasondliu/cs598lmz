import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_cfunctype():
    f = fun()
    raises(AttributeError, getattr, f, 'x')

def test_pycfunction():
    import _testcapi
    f = _testcapi.pycfunction()
    raises(AttributeError, getattr, f, 'x')


class A:
    def __init__(self, value):
        self.value = value

def test_call_a():
    a = A(42)
    raises(TypeError, "a()")
    raises(TypeError, "a(1)")
    raises(TypeError, "a(1, 2)")
    raises(TypeError, "a(1, 2, 3)")
    raises(TypeError, "a(1, 2, 3, 4)")
    raises(TypeError, "a(1, 2, 3, 4, 5)")
    raises(TypeError, "a(1, 2, 3, 4, 5, 6)")
