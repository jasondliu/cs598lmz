import types
# Test types.FunctionType
def func(x):
    return x
assert type(func) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.MethodType
class A:
    def method(self):
        pass
assert type(A.method) == types.MethodType

# Test types.UnboundMethodType
assert type(A.method) == types.UnboundMethodType

# Test types.LambdaType
assert type(lambda x: x) == types.LambdaType

# Test types.GeneratorType
def gen():
    yield 1
assert type(gen()) == types.GeneratorType

# Test types.CodeType
assert type(func.__code__) == types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def f():
    return sys._getframe()
assert type
