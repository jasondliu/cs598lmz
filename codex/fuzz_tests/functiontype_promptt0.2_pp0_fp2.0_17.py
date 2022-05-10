import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
# Test types.LambdaType
g = lambda: None
assert type(g) is types.LambdaType
# Test types.GeneratorType
def h():
    yield
assert type(h()) is types.GeneratorType
# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type(abs) is types.BuiltinFunctionType
# Test types.MethodType
class A:
    def f(self):
        pass
assert type(A().f) is types.MethodType
# Test types.UnboundMethodType
assert type(A.f) is types.UnboundMethodType
# Test types.ModuleType
assert type(types) is types.ModuleType
# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType
# Test types.FrameType
def i():
    assert
