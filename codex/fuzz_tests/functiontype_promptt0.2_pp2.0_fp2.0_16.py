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
class C:
    def m(self):
        pass

assert type(C.m) == types.MethodType
assert isinstance(C.m, types.MethodType)

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
