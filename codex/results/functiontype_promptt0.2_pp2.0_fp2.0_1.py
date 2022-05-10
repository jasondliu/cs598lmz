import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class A:
    def f(self):
        pass

assert type(A.f) == types.MethodType
assert isinstance(A.f, types.MethodType)

# Test types.BuiltinMethodType
assert type(list.append) == types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)

# Test types.ModuleType
import sys
assert type(sys) == types.ModuleType
assert isinstance(sys, types.ModuleType)

# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert type(tb) == types.TracebackType
    assert isinstance(tb, types.Trace
