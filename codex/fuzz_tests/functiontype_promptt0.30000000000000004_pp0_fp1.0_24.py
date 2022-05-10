import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def m(self):
        pass

assert isinstance(C.m, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.m, types.UnboundMethodType)

# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.LambdaType)

# Test types.GeneratorType
def h():
    yield None

assert isinstance(h(), types.GeneratorType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def i():
    pass

assert isinstance(i.__code__.co_frame, types.FrameType)

