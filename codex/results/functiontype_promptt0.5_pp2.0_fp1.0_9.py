import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
def b():
    pass
assert isinstance(b, types.BuiltinFunctionType)

# Test types.GeneratorType
def g():
    yield
assert isinstance(g(), types.GeneratorType)

# Test types.BuiltinMethodType
class C:
    def f(self):
        pass
assert isinstance(C().f, types.BuiltinMethodType)

# Test types.MethodType
class D:
    def f(self):
        pass
assert isinstance(D().f, types.MethodType)

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
assert isinstance(tb.tb_frame, types.FrameType)
