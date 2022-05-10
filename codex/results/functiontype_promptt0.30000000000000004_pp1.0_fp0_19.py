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
    class A:
        def f(self):
            pass
    a = A()
    assert isinstance(a.f, types.MethodType)

# Test types.ModuleType
def test_module_type():
    import sys
    assert isinstance(sys, types.ModuleType)

# Test types.TracebackType
def test_traceback_type():
    try:
        1/0
    except:
        tb = sys.exc_info()[2]
        assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def test_frame_type():
    def f():
        assert isinstance(sys._getframe(), types.FrameType)
    f()


