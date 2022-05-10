import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
assert type(f) is types.BuiltinMethodType
assert type(f) is types.MethodType

# Test types.LambdaType
f = lambda: None
assert type(f) is types.LambdaType

# Test types.GeneratorType
def g(): yield
assert type(g()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
assert type(tb.tb_frame) is types.FrameType

# Test types.BuiltinMethodType
assert type(list.append) is types.BuiltinMethodType

# Test types.ModuleType
assert type(types) is types.ModuleType


