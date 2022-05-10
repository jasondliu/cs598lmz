import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType
assert type(f) == types.BuiltinMethodType
assert type(f) == types.MethodType
assert type(f) == types.UnboundMethodType

# Test types.LambdaType
g = lambda: None
assert type(g) == types.LambdaType

# Test types.GeneratorType
def h():
    yield 1
assert type(h()) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    assert type(sys.exc_info()[2]) == types.TracebackType

# Test types.FrameType
assert type(sys._getframe()) == types.FrameType

# Test types.GetSetDescriptorType
class C(object):
    def __init__(self, x):
        self.x = x
    def getx(self
