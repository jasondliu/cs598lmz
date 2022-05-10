import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_py_object_with_None():
    # This previously crashed.
    def fun():
        pass
    py_object_with_None = (fun, None)
    assert repr(py_object_with_None) == repr((fun, None))
    assert str(py_object_with_None) == repr((fun, None))

def test_py_object_with_None_iter():
    # This previously crashed.
    def fun():
        pass
    py_object_with_None = (fun, None)
    assert list(py_object_with_None) == [fun, None]

def test_py_object_with_None_modify():
    # This previously crashed.
    def fun1():
        pass
    def fun2():
        pass
    py_object_with_None = (fun1, None)
    py_object_with_None[0] = fun2
    assert py_object_with_None == (fun2, None)

def test_py_object_with_None_index():

