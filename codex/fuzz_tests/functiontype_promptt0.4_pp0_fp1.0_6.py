import types
# Test types.FunctionType()
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType()
assert isinstance(abs, types.BuiltinFunctionType)

# Test types.ModuleType()
assert isinstance(types, types.ModuleType)

# Test types.TracebackType()
try:
    raise ValueError
except ValueError:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType()
def g():
    import sys
    return sys._getframe()
assert isinstance(g(), types.FrameType)

# Test types.CodeType()
def h(): pass
assert isinstance(h.__code__, types.CodeType)

# Test types.MethodType()
class C:
    def f(self): pass
assert isinstance(C.f, types.MethodType)

# Test types.UnboundMethodType()
assert isinstance(C.f.__func__, types.UnboundMethod
