import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.LambdaType
g = lambda: None
assert type(g) is types.LambdaType

# Test types.GeneratorType
def h(): yield
assert type(h()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType
assert type(g.__code__) is types.CodeType
assert type(h.__code__) is types.CodeType

# Test types.FrameType
def i():
    assert type(sys._getframe()) is types.FrameType
i()

# Test types.TracebackType
try:
    1/0
except ZeroDivisionError:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.ModuleType
assert type(types) is types.ModuleType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types
