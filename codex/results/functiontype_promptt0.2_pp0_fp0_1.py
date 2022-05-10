import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
assert type(f) != types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(len) != types.FunctionType

# Test types.LambdaType
g = lambda: None
assert type(g) == types.LambdaType
assert type(g) != types.FunctionType
assert type(g) != types.BuiltinFunctionType

# Test types.GeneratorType
def h(): yield None
assert type(h()) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType
assert type(g.__code__) == types.CodeType
assert type(h.__code__) == types.CodeType

# Test types.TracebackType
try:
    1/0
except ZeroDivisionError:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def foo():
    frame
