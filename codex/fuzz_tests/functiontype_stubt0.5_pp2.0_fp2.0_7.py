from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])
d = (x for x in [4])
for i in [a, b, c, d]:
    print(i)

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(isinstance(d, GeneratorType))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))
print(isinstance(d, FunctionType))

print(isinstance(a, type(lambda x: x)))
print(isinstance(b, type(lambda x: x)))
print(isinstance(c, type(lambda x: x)))
print(isinstance(d, type(lambda x: x)))
