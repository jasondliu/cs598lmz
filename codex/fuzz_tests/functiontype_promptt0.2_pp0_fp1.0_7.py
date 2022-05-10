import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType

# Test types.LambdaType
g = lambda: None
assert type(g) == types.LambdaType

# Test types.GeneratorType
def h(): yield
assert type(h()) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType
assert type(g.__code__) == types.CodeType
assert type(h.__code__) == types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
assert type(tb.tb_frame) == types.FrameType

# Test types.BuiltinMethodType
assert type(str.upper) == types.BuiltinMethodType

# Test types.MethodType
class A:
    def
