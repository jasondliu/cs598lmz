import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.MethodType
class C(object):
    def m(self):
        pass
assert isinstance(C.m, types.MethodType)
assert isinstance(C().m, types.MethodType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance("".find, types.BuiltinMethodType)
assert isinstance([].append, types.BuiltinMethodType)
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
    assert isinstance(sys._getframe(), types.FrameType)
g()
# Test types.CodeType
def h(): pass
assert isinstance(h.func_
