import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return rffi.r_long(1)

def test_fun():
    r = fun()
    assert r == 1
test_fun.func_annotations = {}

