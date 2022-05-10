import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"
    assert fun.__name__ == "fun"
    assert fun.__doc__ == None

def test_fun_type():
    assert isinstance(fun, FUNTYPE)
    assert isinstance(fun, ctypes.CFUNCTYPE)
    assert isinstance(fun, ctypes.PyCFuncPtr)
    assert isinstance(fun, ctypes.PyDLL)
    assert isinstance(fun, ctypes.PyCapsule)
    assert isinstance(fun, ctypes.PyObject)
    assert isinstance(fun, ctypes._Pointer)
    assert isinstance(fun, ctypes._CData)
    assert isinstance(fun, ctypes.CData)
    assert isinstance(fun, ctypes.Structure)
    assert isinstance(fun, ctypes.Union)
    assert isinstance(fun, ctypes.Array)
    assert isinstance(fun, ctypes.SimpleType)
    assert isinstance(fun, ctypes._SimpleCData)
   
