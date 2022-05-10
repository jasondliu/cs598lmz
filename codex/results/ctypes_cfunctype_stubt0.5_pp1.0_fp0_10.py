import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return [42]

def test_py_object_return():
    assert fun() == [42]

def test_py_object_return_with_arg():
    def f(x):
        return x
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
    fc = FUNTYPE(f)
    assert fc([42]) == [42]

def test_py_object_return_with_args():
    def f(x, y):
        return x
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
    fc = FUNTYPE(f)
    assert fc([42], [43]) == [42]

def test_py_object_return_with_args2():
    def f(x, y):
        return y
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
   
