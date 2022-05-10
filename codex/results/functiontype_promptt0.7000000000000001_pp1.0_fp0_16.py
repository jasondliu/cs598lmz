import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.LambdaType
l = lambda : None
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
def g():
    yield None
assert isinstance(g(), types.GeneratorType)
isinstance(g(), list)

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.FrameType
def h():
    assert isinstance(sys._getframe(), types.FrameType)
h()

# Test types.MethodType
class A:
    def g(self):
        pass
assert is
