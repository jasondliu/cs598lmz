import types
# Test types.FunctionType
def func(): pass
assert type(func) == types.FunctionType

# Test types.MethodType
class C:
    def method(self): pass
assert type(C().method) == types.MethodType
assert type([].append) == types.MethodType

# Test types.BuiltinMethodType
assert type(list.append) == types.BuiltinMethodType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.ModuleType
import sys
assert type(sys) == types.ModuleType

# Test types.TracebackType
try:
    1/0
except ZeroDivisionError:
    tb = sys.exc_info()[2]
assert type(tb) == types.TracebackType

# Test types.FrameType
def f():
    return sys._getframe()
assert type(f()) == types.FrameType

# Test types.CodeType
assert type(f.func_code) == types.CodeType

# Test types.TypeType
assert type(int) == types.
