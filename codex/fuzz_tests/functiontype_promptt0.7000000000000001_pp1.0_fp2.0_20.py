import types
# Test types.FunctionType
def function():
    pass

print(type(function))
print(type(function) == types.FunctionType)

# Test types.LambdaType
myLambda = lambda x: x*x

print(type(myLambda))
print(type(myLambda) == types.LambdaType)

# Test types.GeneratorType

def gen():
    yield 1

print(type(gen))
print(type(gen()) == types.GeneratorType)

# Test types.MethodType
class MyClass():
    def method(self):
        pass

myObject = MyClass()
myMethod = myObject.method
print(type(myMethod))
print(type(myMethod) == types.MethodType)
