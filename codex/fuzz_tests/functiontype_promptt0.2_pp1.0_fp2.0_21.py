import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
assert type(f) is types.BuiltinMethodType

# Test types.LambdaType
g = lambda: None
assert type(g) is types.LambdaType
assert type(g) is types.FunctionType

# Test types.GeneratorType
def h(): yield
assert type(h()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType
assert type(g.__code__) is types.CodeType
assert type(h.__code__) is types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
def foo():
    frame = sys._getframe()
    assert type(frame) is types.FrameType
foo()

# Test
