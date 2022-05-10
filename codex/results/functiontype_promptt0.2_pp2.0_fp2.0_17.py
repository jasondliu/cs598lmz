import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
# Test types.LambdaType
assert type(lambda: None) is types.LambdaType
# Test types.GeneratorType
def g():
    yield 1
assert type(g()) is types.GeneratorType
# Test types.CodeType
assert type(f.__code__) is types.CodeType
# Test types.FrameType
def h():
    return h.__code__.co_name
assert type(h()) is str
# Test types.TracebackType
try:
    1/0
except ZeroDivisionError:
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
# Test types.MethodType
class
