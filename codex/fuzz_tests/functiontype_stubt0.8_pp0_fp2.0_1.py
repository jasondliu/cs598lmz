from types import FunctionType
a = (x for x in [1])
b = (1 for x in [1])
c = (print for x in [1])
# d = ((yield 1) for x in [1])
e = (lambda x: x for x in [1])

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(isinstance(e, GeneratorType))
# print(isinstance(d, GeneratorType))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))
print(isinstance(e, FunctionType))
# print(isinstance(d, FunctionType))
