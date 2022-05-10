import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
# Test types.LambdaType
l = lambda: None
assert type(l) is types.LambdaType
# Test types.GeneratorType
def g(): yield 1
assert type(g()) is types.GeneratorType
# Test types.CodeType
assert type(f.__code__) is types.CodeType
assert type(l.__code__) is types.CodeType
assert type(g.__code__) is types.CodeType
# Test types.FrameType
def h():
    assert type(sys._getframe()) is types.FrameType
h()
# Test types.TracebackType
try:
    1/0
except ZeroDivisionError:
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType
# Test types.ModuleType
import types
assert type(types) is types.ModuleType
# Test types.BuiltinFunctionType
import sys
assert type(len) is types.BuiltinFunctionType
assert type(sys
