import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType

# Test types.ModuleType
import sys
assert type(sys) == types.ModuleType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType

# Test types.MethodType
class A(object):
    def f(self):
        pass

assert type(A.f) == types.MethodType

# Test types.UnboundMethodType
assert type(A.f) == types.MethodType

# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    assert type(sys.exc_info()[2]) == types.TracebackType

# Test types.FrameType
import sys
assert type(sys._getframe()) == types.FrameType

# Test types.CodeType
def f():
    pass

assert type(f.func_code) == types.CodeType

# Test types
