import types
# Test types.FunctionType
def f(): pass
assert type(f) == types.FunctionType

# Test types.LambdaType
g = lambda x: x
assert type(g) == types.LambdaType

# Test types.GeneratorType
def h():
    yield 1
    yield 2

assert type(h()) == types.GeneratorType

# Test types.CodeType
assert type(f.__code__) == types.CodeType
assert type(g.__code__) == types.CodeType
assert type(h.__code__) == types.CodeType

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType

# Test types.FrameType
def i():
    assert type(sys._getframe()) == types.FrameType
i()

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.
