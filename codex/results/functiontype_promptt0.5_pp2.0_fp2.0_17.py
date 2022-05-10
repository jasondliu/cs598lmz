import types
# Test types.FunctionType
def test_function():
    def fn():
        pass
    assert isinstance(fn, types.FunctionType)

# Test types.MethodType
def test_method():
    class A:
        def fn(self):
            pass
    a = A()
    assert isinstance(a.fn, types.MethodType)

# Test types.BuiltinFunctionType
def test_builtin_function():
    assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
def test_builtin_method():
    assert isinstance([].append, types.BuiltinMethodType)
    assert isinstance({}.get, types.BuiltinMethodType)

# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)

# Test types.TracebackType
import sys
try:
    raise Exception
except:
    etype, value, tb = sys.exc_info()
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
import sys
try:

