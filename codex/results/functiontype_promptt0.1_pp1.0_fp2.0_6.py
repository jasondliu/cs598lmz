import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.MethodType
class C:
    def m(self):
        pass
assert type(C.m) == types.MethodType

# Test types.UnboundMethodType
assert type(C.m) == types.UnboundMethodType

# Test types.LambdaType
assert type(lambda: None) == types.LambdaType

# Test types.GeneratorType
assert type((x for x in range(10))) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    assert type(sys.exc_info()[2]) == types.TracebackType

# Test types.FrameType
assert type(sys._getframe()) == types.Frame
