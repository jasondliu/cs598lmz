from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(isinstance(a, GeneratorType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance(lambda x: x, GeneratorType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance(lambda x: x, object))
print(isinstance(lambda x: x, (object,)))
print(isinstance(a, (object,)))
print(isinstance(a, (GeneratorType,)))
print(isinstance(a, (GeneratorType, object)))
print(isinstance(a, (object, GeneratorType)))
print(isinstance(a, (GeneratorType, FunctionType)))
print(isinstance(a, (FunctionType, GeneratorType)))

print('-' * 100)

print(isinstance(a, (FunctionType,)))
print(isinstance(a, (FunctionType, object)))
print(isinstance(a, (object, FunctionType)))
print(isinstance(a, (FunctionType, GeneratorType)))
print(isinstance(
