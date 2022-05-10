import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello, world"

def test_fun():
    assert fun() == "Hello, world"

