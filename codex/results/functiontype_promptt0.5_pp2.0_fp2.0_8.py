import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(int, types.FunctionType)

# Test types.BuiltinFunctionType
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(lambda: None, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def meth(self): pass
assert isinstance(C().meth, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.meth, types.UnboundMethodType)

# Test types.BuiltinMethodType
assert isinstance(int.__add__, types.BuiltinMethodType)

# Test types.ModuleType
import sys
assert isinstance(sys, types.ModuleType)
assert not isinstance(sys.modules, types.ModuleType)

# Test types.TracebackType
import sys
try:
    raise Exception
except:
    e =
