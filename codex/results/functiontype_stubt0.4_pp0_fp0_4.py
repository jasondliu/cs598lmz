from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(int))
print(type(FunctionType))

import inspect
print(inspect.isgeneratorfunction(a))
print(inspect.isgeneratorfunction(int))
print(inspect.isgeneratorfunction(FunctionType))

print(isinstance(a, FunctionType))
print(isinstance(int, FunctionType))
print(isinstance(FunctionType, FunctionType))
print(isinstance(a, type))
print(isinstance(int, type))
print(isinstance(FunctionType, type))

print(isinstance(a, (FunctionType, type)))
print(isinstance(int, (FunctionType, type)))
print(isinstance(FunctionType, (FunctionType, type)))

print(issubclass(type, object))
print(issubclass(FunctionType, object))
print(issubclass(FunctionType, type))
print(issubclass(type, FunctionType))

print(issubclass(type, (FunctionType, object)))
print(issubclass(FunctionType, (FunctionType, object
