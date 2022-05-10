import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) == types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.MethodType
class C:
    def m(self): pass
assert type(C.m) is types.MethodType
assert type(C().m) == types.MethodType

# Test types.BuiltinMethodType
assert type(list.append) is types.BuiltinMethodType
assert type(list().append) == types.BuiltinMethodType

# Test types.ModuleType
assert type(types) is types.ModuleType
assert type(types) == types.ModuleType

# Test types.TracebackType
import sys
try:
    raise Exception()
except:
    tb = sys.exc_info()[2]
assert type(tb) is types.TracebackType
assert type(tb) == types.TracebackType

# Test types.FrameType
import
