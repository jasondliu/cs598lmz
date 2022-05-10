import types
# Test types.FunctionType
def test_FunctionType():
    def f():
        pass
    assert type(f) is types.FunctionType
    assert isinstance(f, types.FunctionType)
    assert not issubclass(types.FunctionType, object)

# Test types.BuiltinFunctionType
def test_BuiltinFunctionType():
    assert type(map) is types.BuiltinFunctionType
    assert isinstance(map, types.BuiltinFunctionType)
    assert not issubclass(types.BuiltinFunctionType, object)

# Test types.BuiltinMethodType
def test_BuiltinMethodType():
    assert type(str.lower) is types.BuiltinMethodType
    assert isinstance(str.lower, types.BuiltinMethodType)
    assert not issubclass(types.BuiltinMethodType, object)

# Test types.ModuleType
def test_ModuleType():
    import sys
    assert type(sys) is types.ModuleType
    assert isinstance(sys, types.ModuleType)
    assert not issubclass(types.ModuleType, object)

# Test types.Method
