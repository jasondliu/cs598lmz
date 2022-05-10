import types
# Test types.FunctionType
def test(c,d):
    pass
print(type(test))
# function
print(type(test) == types.FunctionType)
# True

# for python2
# print(type(test) == types.LambdaType)
# False

# Test types.LambdaType
f = lambda a: a + 1
print(type(f))
# function
print(type(f) == types.LambdaType)
# True

# Test types.GeneratorType
g = (x for x in range(1,11))
print(type(g))
# generator
print(type(g) == types.GeneratorType)
# True

# Test types.GeneratorType
class MyClass:
    def __init__(self):
        pass
    def __call__(self):
        pass
obj = MyClass()
print(type(obj))
# class '__main__.MyClass'
print(type(obj) == types.FunctionType)
# False

print(type(test) == types.BuiltinFunctionType)
#
