import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.MethodType
class C(object):
    def f(self):
        pass

assert isinstance(C.f, types.MethodType)
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
assert isinstance(f.__code__, types.CodeType)
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
# Test types.FrameType
def ff():
    assert isinstance(
