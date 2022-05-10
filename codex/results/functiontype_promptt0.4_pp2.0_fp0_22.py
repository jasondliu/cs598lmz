import types
# Test types.FunctionType
def func(x):
    return x

print(type(func) is types.FunctionType)
print(type(lambda x: x) is types.FunctionType)
print(type(func) is types.LambdaType)

# Test types.BuiltinFunctionType
print(type(abs) is types.BuiltinFunctionType)
print(type(func) is types.BuiltinFunctionType)

# Test types.GeneratorType
def gen():
    yield 1

print(type(gen()) is types.GeneratorType)

# Test types.GeneratorType
class A:
    pass

print(type(A) is types.ClassType)
print(type(A()) is types.InstanceType)

# Test types.MethodType
class B:
    def method(self):
        pass

print(type(B.method) is types.MethodType)
print(type(B().method) is types.MethodType)

# Test types.UnboundMethodType
print(type(B.method) is types.UnboundMethodType)
print(type(
