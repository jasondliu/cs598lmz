import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
# Test types.LambdaType
g = lambda x: x
assert type(g) == types.LambdaType
# Test types.GeneratorType
h = (x for x in range(10))
assert type(h) == types.GeneratorType

# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType

# Test types.MethodType
class A:
    def f(self):
        pass
assert type(A().f) == types.MethodType

# Test types.UnboundMethodType
assert type(A.f) == types.UnboundMethodType

# Test types.TracebackType
try:
    raise Exception
except Exception:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def f():
    return sys._getframe
