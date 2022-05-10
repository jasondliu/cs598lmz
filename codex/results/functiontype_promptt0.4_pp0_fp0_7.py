import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.MethodType
class A:
    def f(self): pass
assert type(A.f) is types.MethodType
assert type(A().f) is types.MethodType

# Test types.UnboundMethodType
assert type(A.f) is types.MethodType

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType

# Test types.GeneratorType
assert type((lambda: (yield))()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.FrameType
assert type(sys._getframe()) is types.FrameType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
assert type(tb) is types.TracebackType

#
