import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass

def f(x):
    return x

def test_func_type():
    ftype = type(f)
    assert isinstance(ftype, types.FunctionType)
    assert issubclass(ftype, types.FunctionType)
    assert not isinstance(ftype, types.MethodType)
    assert not issubclass(ftype, types.MethodType)

    assert isinstance(f, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(f, types.BuiltinMethodType)
    assert not isinstance(f, types.MethodType)
    assert not isinstance(f, types.LambdaType)

    assert isinstance(fun, types.FunctionType)
    assert not isinstance(fun, types.BuiltinFunctionType)
    assert not isinstance(fun, types.BuiltinMethodType)
    assert not isinstance(fun, types.MethodType)
    assert not isinstance(fun, types.LambdaType)

    assert not isinstance(lambda: None, types.Function
