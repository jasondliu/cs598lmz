import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
def g():
    yield
assert isinstance(g(), types.GeneratorType)

# Test types.MethodType
class C:
    def m(self):
        pass
assert isinstance(C().m, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.m, types.UnboundMethodType)

# Test types.ModuleType
assert isinstance(types, types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except Exception:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def f():
    import sys
