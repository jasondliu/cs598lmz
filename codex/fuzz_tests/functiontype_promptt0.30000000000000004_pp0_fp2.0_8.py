import types
# Test types.FunctionType
def f():
    pass

assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
assert type(f) is types.BuiltinMethodType

# Test types.LambdaType
l = lambda x: x
assert type(l) is types.LambdaType

# Test types.GeneratorType
g = (x for x in range(3))
assert type(g) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType
assert type(l.__code__) is types.CodeType
assert type(g.gi_code) is types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
assert type(tb.tb_frame) is types.FrameType

# Test types.BuiltinFunctionType
assert type(abs)
