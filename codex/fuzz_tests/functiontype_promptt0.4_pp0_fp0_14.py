import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def f(self):
        pass

assert isinstance(C().f, types.MethodType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
def g():
    yield None

assert isinstance(g(), types.GeneratorType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.CodeType
def f():
    pass

assert isinstance(f.__code__, types.CodeType)

# Test types.FrameType
def f():
    assert isinstance(sys._getframe(), types.FrameType)

f
