import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def f(self):
        pass

assert isinstance(C().f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.f, types.UnboundMethodType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1

assert isinstance(g(), types.GeneratorType)

# Test types.CodeType
assert isinstance(g.__code__, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
assert isinstance(
