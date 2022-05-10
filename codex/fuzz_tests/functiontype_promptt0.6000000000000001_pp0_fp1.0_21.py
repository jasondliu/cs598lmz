import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def f(self):
        pass
assert isinstance(C.f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.f, types.UnboundMethodType)

# Test types.LambdaType
x = lambda: None
assert isinstance(x, types.LambdaType)

# Test types.GeneratorType
def g():
    yield
assert isinstance(g(), types.GeneratorType)

# Test types.CodeType
def f(): pass
assert isinstance(f.__code__, types.CodeType)

# Test types.FrameType
def f():
    assert isinstance(_getframe(0), types.FrameType)
f()

# Test types.TracebackType
def f():
    try:
        1/0
    except:
        import sys
