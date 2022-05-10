import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
assert type(f) is types.BuiltinMethodType
assert type(f) is types.MethodType

# Test types.LambdaType
l = lambda: None
assert type(l) is types.LambdaType

# Test types.GeneratorType
g = (i for i in range(10))
assert type(g) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
def g():
    return sys._getframe()
assert type(g()) is types.FrameType

# Test types.SliceType
assert type(slice(1)) is types.SliceType

# Test types.EllipsisType

