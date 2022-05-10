import types
# Test types.FunctionType
def foo():
    pass
assert isinstance(foo, types.FunctionType)

# Test types.ClassType
class A:
    pass
assert isinstance(A, types.ClassType)

# Test types.InstanceType
a = A()
assert isinstance(a, types.InstanceType)

# Test types.MethodType
def foo():
    pass
assert isinstance(A.foo, types.MethodType)

# Test types.GeneratorType
def foo():
    yield 1
assert isinstance(foo(), types.GeneratorType)

# Test types.TracebackType
import sys
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.CodeType
assert isinstance(foo.func_code, types.CodeType)

# Test types.FrameType
import sys
assert isinstance(sys._getframe(), types.FrameType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunction
