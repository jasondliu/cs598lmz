import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def f(self):
        pass

assert isinstance(C.f, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance(C.__init__, types.BuiltinMethodType)

# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except:
    e, v, tb = sys.exc_info()
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
def f():
    return sys._getframe()

assert isinstance(f(), types.FrameType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.GeneratorType
def g():
    yield
