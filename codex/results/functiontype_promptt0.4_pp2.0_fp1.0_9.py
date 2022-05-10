import types
# Test types.FunctionType
def a():
    pass

print isinstance(a, types.FunctionType)

# Test types.BuiltinFunctionType
print isinstance(len, types.BuiltinFunctionType)

# Test types.ClassType
class A:
    pass

print isinstance(A, types.ClassType)

# Test types.TypeType
print isinstance(A, types.TypeType)

# Test types.UnboundMethodType
print isinstance(A.__init__, types.UnboundMethodType)

# Test types.InstanceType
a = A()
print isinstance(a, types.InstanceType)

# Test types.LambdaType
print isinstance((lambda x: x), types.LambdaType)

# Test types.GeneratorType
def b():
    yield 1

print isinstance(b(), types.GeneratorType)

# Test types.TracebackType
import sys
print isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.CodeType
print isinstance(a.__code__
