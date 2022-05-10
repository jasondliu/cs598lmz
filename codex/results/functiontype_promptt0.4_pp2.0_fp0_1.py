import types
# Test types.FunctionType
def test_function():
    def func(): pass
    assert isinstance(func, types.FunctionType)
    assert not isinstance(func, types.BuiltinFunctionType)
    assert not isinstance(func, types.MethodType)
    assert not isinstance(func, types.BuiltinMethodType)

    class A:
        def func(self): pass
    assert isinstance(A.func, types.MethodType)
    assert not isinstance(A.func, types.BuiltinMethodType)
    assert not isinstance(A.func, types.FunctionType)
    assert not isinstance(A.func, types.BuiltinFunctionType)

    class A:
        def func(self): pass
        func = classmethod(func)
    assert isinstance(A.func, types.MethodType)
    assert not isinstance(A.func, types.BuiltinMethodType)
    assert not isinstance(A.func, types.FunctionType)
    assert not isinstance(A.func, types.BuiltinFunctionType)

    class A:
        def func(self): pass
       
