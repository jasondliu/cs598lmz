import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)

# Test types.MethodType
class A:
    def f(self): pass

assert isinstance(A().f, types.MethodType)

# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except:
    exc = sys.exc_info()[2]
assert isinstance(exc, types.TracebackType)

# Test types.FrameType
import inspect
assert isinstance(inspect.currentframe(), types.FrameType)

# Test types.GetSetDescriptorType
class A:
    x = 1

assert isinstance(A.__dict__['x'],
