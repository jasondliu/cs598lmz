import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5

def test_makefun_1():
    func = helper.make_function(fun)
    res = func()
    assert res == 5
