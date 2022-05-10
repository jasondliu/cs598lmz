import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_funtype():
    assert fun() == "hello"

def test_funtype_with_docstring():
    """
    This test is for issue #15.
    """
    def f(x):
        """
        Some docstring.
        """
        return x
    FUNTYPE2 = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
    g = FUNTYPE2(f)
    assert g.__doc__ == f.__doc__

def test_funtype_with_defaults():
    """
    This test is for issue #16.
    """
    def f(x, y=42):
        return x + y
    FUNTYPE2 = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object,
                                ctypes.py_object)
    g = FUNTYPE2(f)
    assert g(1) == 43
    assert g(1, 2) == 3

def test_funtype_with_kwargs():
