import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType
class A:
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(A.f.__func__, types.UnboundMethodType)

# Test types.ModuleType
import math
assert isinstance(math, types.ModuleType)

# Test types.TracebackType
import sys
assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.FrameType
assert isinstance(sys._getframe(), types.FrameType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.SimpleNamespace
ns = types.SimpleNamespace(a=1, b=2)
