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
assert type(C.m.__func__) == types.UnboundMethodType

# Test types.LambdaType
assert type(lambda: None) == types.LambdaType

# Test types.GeneratorType
assert type((lambda: (yield))()) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def f():
    frame = sys._getframe()
    assert type(
