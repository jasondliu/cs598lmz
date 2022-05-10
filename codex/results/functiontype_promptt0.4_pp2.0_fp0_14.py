import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class Foo:
    def __init__(self, x):
        self.x = x
    def f(self):
        return self.x
foo = Foo(42)
assert isinstance(foo.f, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance(foo.__init__, types.BuiltinMethodType)

# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except:
    exc_info = sys.exc_info()
    assert isinstance(exc_info[2], types.TracebackType)

# Test types.FrameType
def g():
    assert isinstance(sys._getframe(), types.FrameType)
g()

# Test types.CodeType
assert isinstance(g.
