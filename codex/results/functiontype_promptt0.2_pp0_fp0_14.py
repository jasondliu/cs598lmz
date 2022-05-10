import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
# Test types.LambdaType
g = lambda x: x
assert type(g) == types.LambdaType
# Test types.GeneratorType
def h():
    yield 1
assert type(h()) == types.GeneratorType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType
# Test types.MethodType
class A:
    def f(self):
        pass
assert type(A().f) == types.MethodType
# Test types.UnboundMethodType
assert type(A.f) == types.UnboundMethodType
# Test types.ModuleType
import sys
assert type(sys) == types.ModuleType
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType
# Test types.FrameType
