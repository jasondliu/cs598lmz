import types
# Test types.FunctionType
def fn(): pass
class A(object):
    def m(self): pass

assert type(fn) is types.FunctionType
assert type(fn) is types.FunctionType
assert type(A.m) is types.MethodType
assert type(A.m) is types.MethodType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type(str.upper) is types.BuiltinMethodType
assert type(str.upper) is types.BuiltinMethodType

# Test types.ModuleType
import sys
assert type(sys) is types.ModuleType
assert type(sys) is types.ModuleType

# Test types.TracebackType
try: 1/0
except: tb = sys.exc_info()[2]
assert type(tb) is types.TracebackType
assert type(tb) is types.TracebackType

# Test types.FrameType
def g():
    assert type(sys._
