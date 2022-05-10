import types
# Test types.FunctionType
def func(x):
    return x

print(type(func) is types.FunctionType)

# Test types.LambdaType
x = lambda x: x
print(type(x) is types.LambdaType)

# Test types.GeneratorType
def generator():
    for i in range(10):
        yield i

g = generator()
print(type(g) is types.GeneratorType)

# Test types.GeneratorType
class A(object):
    pass

print(type(A) is types.TypeType)

# Test types.ClassType
class B:
    pass

print(type(B) is types.ClassType)

# Test types.InstanceType
a = A()
print(type(a) is types.InstanceType)

# Test types.MethodType
print(type(A.__init__) is types.MethodType)
print(type(a.__init__) is types.MethodType)

# Test types.BuiltinFunctionType
print(type(len) is types.BuiltinFunctionType
