import types
# Test types.FunctionType
assert isinstance(reverse, types.FunctionType)

# Test types.GeneratorType
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fib()
assert isinstance(f, types.GeneratorType)

# Test types.ModuleType
import types
assert isinstance(types, types.ModuleType)

# Test types.TracebackType
import sys
assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.FrameType
import sys
assert isinstance(sys._getframe(), types.FrameType)

# Test types.TypeType
assert isinstance(types.ModuleType, types.TypeType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance(sys.exit, type(sys.exit))
assert isinstance(sys.exit, types.BuiltinMethodType)

# Test types.MethodType
def f
