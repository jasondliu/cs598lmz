import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType

# Test types.LambdaType
g = lambda x: x
assert type(g) is types.LambdaType

# Test types.GeneratorType
def h():
    yield 1
assert type(h()) is types.GeneratorType

# Test types.MethodType
class A:
    def f(self):
        pass
assert type(A().f) is types.MethodType

# Test types.BuiltinMethodType
assert type(A.f) is types.BuiltinMethodType

# Test types.UnboundMethodType
assert type(A.f) is types.UnboundMethodType

# Test types.TracebackType
try:
    raise Exception
except Exception:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
def f():
    return sys._getframe()
assert type(f()) is types.Frame
