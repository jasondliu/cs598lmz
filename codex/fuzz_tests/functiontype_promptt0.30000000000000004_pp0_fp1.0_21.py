import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
# Test types.MethodType
class A:
    def f(self):
        pass
assert type(A.f) == types.MethodType
assert type(A().f) == types.MethodType
# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType
assert type({}.get) == types.BuiltinMethodType
# Test types.ModuleType
import sys
assert type(sys) == types.ModuleType
# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType
# Test types.FrameType
def g():
    return sys._getframe()
assert type(g()) == types.FrameType
# Test types.CodeType
def h(): pass
assert type(h.__code__) == types.CodeType
# Test types.
