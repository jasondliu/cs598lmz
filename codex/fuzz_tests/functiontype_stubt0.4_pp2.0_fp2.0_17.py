from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(type(a))
print(type(b))
print(type(a) is type(b))
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

print(type(a) == type(b))
print(a == b)

print(isinstance(a, (GeneratorType, FunctionType)))
print(isinstance(b, (GeneratorType, FunctionType)))

print(isinstance(a, (FunctionType, GeneratorType)))
print(isinstance(b, (FunctionType, GeneratorType)))

print(isinstance(a, (FunctionType, GeneratorType, object)))
print(isinstance(b, (FunctionType, GeneratorType, object)))

print(isinstance(a, (object, FunctionType, GeneratorType)))
print(isinstance(b, (object, FunctionType, GeneratorType)))

print(isinstance(a, (FunctionType,
