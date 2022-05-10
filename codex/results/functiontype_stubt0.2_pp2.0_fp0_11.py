from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))

print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

print(isinstance(lambda x: x, FunctionType))
print(isinstance(lambda x: x, Function))
print(isinstance(lambda x: x, object))
print(isinstance(lambda x: x, type))

print(isinstance(FunctionType, type))
print(isinstance(Function, type))

print(isinstance(FunctionType, object))
print(isinstance(Function, object))

print(isinstance(FunctionType, Function))
print(isinstance(Function, Function))

print(isinstance(FunctionType, FunctionType))
print(isinstance(Function, FunctionType))

print(isinstance(FunctionType, type))
print(isinstance(Function, type))

print(isinstance(FunctionType, object))
print(isinstance(Function, object))

print(isinstance(Function
