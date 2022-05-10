import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
# Test types.MethodType
class C:
    def f(self): pass
assert type(C.f) is types.MethodType
assert type(C().f) is types.MethodType
# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType
# Test types.BuiltinMethodType
class C:
    def f(self): pass
assert type(C.f) is types.MethodType
assert type(C().f) is types.MethodType
# Test types.ModuleType
import types
assert type(types) is types.ModuleType
# Test types.TracebackType
def f():
    raise Exception
try:
    f()
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType
# Test types.FrameType
def f(): pass
assert type(f.__code__.co_consts[0]) is types.FrameType
# Test types.CodeType
def f
