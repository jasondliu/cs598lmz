import types
# Test types.FunctionType
def test_function_type():
    def f():
        pass
    assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
def test_method_type():
    class C:
        def m(self):
            pass
    assert isinstance(C().m, types.MethodType)

# Test types.BuiltinMethodType
def test_builtin_method_type():
    assert isinstance([].append, types.BuiltinMethodType)

# Test types.ModuleType
def test_module_type():
    import sys
    assert isinstance(sys, types.ModuleType)

# Test types.TracebackType
def test_traceback_type():
    try:
        1 / 0
    except Exception as e:
        tb = e.__traceback__
        assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def test_
