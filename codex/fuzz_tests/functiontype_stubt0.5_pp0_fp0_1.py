from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))

b = (x for x in [1])
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
print(isinstance(b, Iterator))

print(isinstance(a, b))
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
