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

# Test types.FrameType
def i():
    assert type(sys._getframe()) is types.FrameType
i()

# Test types.TracebackType
try:
    raise Exception
except:
    assert type(sys.exc_info()[2]) is types.TracebackType

# Test types.ModuleType
assert type(sys) is types.ModuleType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.BuiltinMethodType

