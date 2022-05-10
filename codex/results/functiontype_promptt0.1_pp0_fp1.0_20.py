import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
# Test types.MethodType
class A:
    def f(self):
        pass
assert type(A().f) == types.MethodType
# Test types.UnboundMethodType
assert type(A.f) == types.UnboundMethodType
# Test types.LambdaType
assert type(lambda: None) == types.LambdaType
# Test types.GeneratorType
def g():
    yield 1
assert type(g()) == types.GeneratorType
# Test types.CodeType
assert type(f.__code__) == types.CodeType
# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType
# Test types.FrameType
def h():
    assert type(sys._getframe()) == types.FrameType
h()
# Test types.Get
