import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def m(self):
        pass

assert isinstance(C.m, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.m, types.UnboundMethodType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)

# Test types.GeneratorType
g = (i for i in range(10))
assert isinstance(g, types.GeneratorType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def g():
    assert isinstance(sys._getframe(), types.FrameType)
g()

#
