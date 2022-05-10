import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType

# Test types.BuiltinFunctionType
assert type(abs) == types.BuiltinFunctionType

# Test types.MethodType
class A:
    def f(self):
        pass

assert type(A.f) == types.MethodType

# Test types.UnboundMethodType
assert type(A.f) == types.MethodType

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
    assert type(sys.exc_info()[2]) == types.TracebackType

# Test types.FrameType
assert type(sys._getframe()) == types.FrameType
