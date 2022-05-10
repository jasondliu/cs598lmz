import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
# Test types.MethodType
class C:
    def m(self):
        pass
assert isinstance(C().m, types.MethodType)
assert not isinstance(C().m, types.FunctionType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
assert not isinstance([].append, types.MethodType)
# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
# Test types.FrameType
def g():
    return sys._getframe()
assert isinstance(g
