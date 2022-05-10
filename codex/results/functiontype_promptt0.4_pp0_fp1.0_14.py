import types
# Test types.FunctionType
def func1(): pass
def func2(arg): pass
def func3(arg1, arg2): pass
def func4(arg1, arg2=None): pass
def func5(arg1, *args): pass
def func6(arg1, **kwargs): pass
def func7(arg1, *args, **kwargs): pass
def func8(arg1, arg2=None, *args, **kwargs): pass

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(abs, types.BuiltinFunctionType)
    assert isinstance(chr, types.BuiltinFunctionType)
    assert isinstance(divmod, types.BuiltinFunctionType)
    assert isinstance(enumerate, types.BuiltinFunctionType)
    assert isinstance(filter, types.BuiltinFunctionType)
    assert isinstance(hex, types.BuiltinFunctionType)
    assert isinstance(id, types.BuiltinFunctionType)
    assert isinstance(int, types.BuiltinFunctionType)
    assert isinstance(iter,
