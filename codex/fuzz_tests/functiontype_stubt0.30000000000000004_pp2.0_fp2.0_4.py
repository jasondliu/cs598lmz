from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(a, object))
print(isinstance(b, object))

print(isinstance(a, (GeneratorType, FunctionType)))
print(isinstance(b, (GeneratorType, FunctionType)))

print(isinstance(a, (GeneratorType, FunctionType, object)))
print(isinstance(b, (GeneratorType, FunctionType, object)))

print(isinstance(a, (GeneratorType, FunctionType, object)))
print(isinstance(b, (GeneratorType, FunctionType, object)))

print(isinstance(a, (GeneratorType, FunctionType, object)))
print(isinstance(b, (GeneratorType, FunctionType, object)))

print
