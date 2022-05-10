import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType

# Test types.MethodType
class C:
    def f(self):
        pass
assert type(C().f) == types.MethodType

# Test types.UnboundMethodType
assert type(C.f) == types.UnboundMethodType

# Test types.LambdaType
assert type(lambda x: x) == types.LambdaType

# Test types.GeneratorType
def g():
    yield 1
assert type(g()) == types.GeneratorType

# Test types.CodeType
assert type(g.__code__) == types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
assert type(tb.tb_frame) == types.FrameType


