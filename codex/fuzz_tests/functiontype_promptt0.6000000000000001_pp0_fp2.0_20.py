import types
# Test types.FunctionType

# FunctionType is a class
# this is a function object
def foo():
    pass

print(type(foo))
print(foo)
print(foo.__class__)
print(type(foo) == foo.__class__)
print(type(foo) == types.FunctionType)
print(isinstance(foo, types.FunctionType))
print(isinstance(foo, types.FunctionType))

print("------------------")

# this is not a function object
foo1 = lambda x: x**2
print(type(foo1))
print(foo1)
print(foo1.__class__)
print(type(foo1) == foo1.__class__)
print(type(foo1) == types.FunctionType)
print(isinstance(foo1, types.FunctionType))
print(isinstance(foo1, types.FunctionType))

print("------------------")

# this is not a function object
foo2 = lambda x: x**2
print(type(foo2))
print(foo2)
print(foo2.__class__)
