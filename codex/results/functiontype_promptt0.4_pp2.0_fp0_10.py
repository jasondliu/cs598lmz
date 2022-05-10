import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(dir, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def f(self): pass
assert isinstance(C.f, types.MethodType)
assert isinstance(C().f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.f, types.UnboundMethodType)
assert not isinstance(C().f, types.UnboundMethodType)

# Test types.LambdaType
assert isinstance((lambda: None), types.LambdaType)

# Test types.GeneratorType
assert isinstance((x for x in range(5)), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.FrameType
def g():
    assert isinstance(sys._getframe(), types.FrameType)
g()

# Test types.TracebackType
try:

