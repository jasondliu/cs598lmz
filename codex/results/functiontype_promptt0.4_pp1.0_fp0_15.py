import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType

# Test types.LambdaType
g = lambda x: x+1
assert type(g) is types.LambdaType

# Test types.GeneratorType
def h():
    yield 1
    yield 2

assert type(h) is types.GeneratorType
assert type(h()) is types.GeneratorType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.CodeType
def i(): pass
assert type(i.__code__) is types.CodeType

# Test types.FrameType
import sys
assert type(sys._getframe()) is types.FrameType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
assert type({}.get) is
