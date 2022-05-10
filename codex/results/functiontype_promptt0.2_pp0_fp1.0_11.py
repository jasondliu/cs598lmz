import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
# Test types.MethodType
class C:
    def f(self):
        pass
assert type(C.f) == types.MethodType
assert type(C().f) == types.MethodType
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
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType
# Test types.FrameType
def f():
    import sys
    return sys._getframe()
assert type(f()) == types.FrameType
# Test types.CodeType
def f(): pass
assert type(f.__code__) == types
