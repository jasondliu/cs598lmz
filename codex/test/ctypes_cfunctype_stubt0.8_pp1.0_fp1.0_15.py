import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    y = 'XX'
    return y

def test_fun():
    x = fun()
    assert x == 'XX'
