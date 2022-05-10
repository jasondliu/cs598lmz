import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
# Test types.LambdaType
g = lambda x: x
assert type(g) is types.LambdaType
# Test types.GeneratorType
def h():
    yield 1
assert type(h()) is types.GeneratorType
# Test types.CodeType
assert type(h.__code__) is types.CodeType
# Test types.FrameType
def i():
    return i.__code__.__class__
assert type(i()) is types.FrameType
# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType
# Test types.ModuleType
import sys
assert type(sys) is types.ModuleType
# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
# Test types.
