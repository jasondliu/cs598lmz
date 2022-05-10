import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

def test_add():
    assert(add(1,2) == 3)

def test_subtract():
    assert(subtract(1,2) == -1)

def test_multiply():
    assert(multiply(1,2) == 2)

def test_divide():
    assert(divide(1,2) == 0.5)
