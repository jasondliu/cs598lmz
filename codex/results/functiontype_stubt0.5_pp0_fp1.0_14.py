from types import FunctionType
a = (x for x in [1])
print(type(a))

def a():
    pass

print(type(a))
print(type(a) is FunctionType)
print(type(a) == FunctionType)

print(type(a) == types.GeneratorType)

print(isinstance(a, FunctionType))
print(isinstance(a, types.GeneratorType))

print(isinstance(a(), types.GeneratorType))
print(isinstance(a(), FunctionType))

# print(dir(a))

print(dir(type))

# print(dir(types))

# print(dir(__builtins__))

def a():
    pass

print(dir(a))

print(a.__name__)

def a():
    pass

print(a.__name__)

print(a.__dict__)

print(type.__dict__)

print(type.__dict__['__call__'])

print(type.__call__)

print(type.__call__ is type.__dict__['
