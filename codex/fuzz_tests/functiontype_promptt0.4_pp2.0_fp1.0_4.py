import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.MethodType
class A:
    def f(self):
        pass
assert isinstance(A.f, types.MethodType)
assert isinstance(A().f, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
assert isinstance([].__len__, types.BuiltinMethodType)

# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def f():
    import sys
    return sys._getframe()
assert isinstance(f(), types.FrameType)

# Test types.
