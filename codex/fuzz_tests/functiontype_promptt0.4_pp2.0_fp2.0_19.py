import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)

# Test types.MethodType
class C:
    def m(self):
        pass

c = C()
assert isinstance(c.m, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)

# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def f():
    import sys
    return sys._getframe()

assert isinstance(f(), types.FrameType)

# Test types.GetSetDescriptorType
class C:
    def fget(self):
        pass
    def
