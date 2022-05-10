import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type(str.upper) is types.BuiltinMethodType
assert type(str.upper) is types.MethodType

# Test types.MethodType
class A:
    def f(self): pass
assert type(A().f) is types.MethodType

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType

# Test types.GeneratorType
assert type((lambda: (yield))()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    1 / 0
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
def g():
    frame = sys._getframe()
    assert type(frame) is types.
