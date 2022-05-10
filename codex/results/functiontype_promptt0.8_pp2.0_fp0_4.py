import types
# Test types.FunctionType
class MyClass:
    pass

def func1(x):
    return x

obj = MyClass()

obj.func2 = func1

print(type(func1))
print(type(obj.func2))

print(type(obj.func2) == types.FunctionType)
print(type(obj.func2) is types.FunctionType)
# Test types.LambdaType

func3 = lambda x: x*x

print(type(func3))
print(type(func3) == types.LambdaType)
print(type(func3) is types.LambdaType)
# Test types.ClassType

print(type(MyClass))
print(type(MyClass) == types.ClassType)
print(type(MyClass) is types.ClassType)
# Test types.InstanceType

obj = MyClass()

print(type(obj))
print(type(obj) == types.InstanceType)
print(type(obj) is types.InstanceType)
# Test types.GeneratorType

def func4(
