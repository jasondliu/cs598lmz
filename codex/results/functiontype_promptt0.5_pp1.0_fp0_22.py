import types
# Test types.FunctionType:
def f(x): return x + 1
assert type(f) == types.FunctionType
assert type(f(1)) == int
# Test types.MethodType:
class C:
    def f(self): return 42
assert type(C.f) == types.FunctionType
assert type(C().f) == types.MethodType
# Test types.BuiltinFunctionType:
assert type(len) == types.BuiltinFunctionType
assert type(len([1, 2, 3])) == int
# Test types.BuiltinMethodType:
assert type([1, 2, 3].index) == types.BuiltinMethodType
assert type([1, 2, 3].index(1)) == int
# Test types.ModuleType:
import sys
assert type(sys) == types.ModuleType
# Test types.TracebackType:
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType
# Test types.FrameType:
def f():
    return sys._getframe()

