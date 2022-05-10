import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.MethodType
class C:
    def m(self):
        pass
assert type(C.m) == types.MethodType

# Test types.UnboundMethodType
assert type(C.m.__get__(None, C)) == types.UnboundMethodType

# Test types.LambdaType
l = lambda: None
assert type(l) == types.LambdaType

# Test types.GeneratorType
def g():
    yield
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
def ff():
    return sys._get
