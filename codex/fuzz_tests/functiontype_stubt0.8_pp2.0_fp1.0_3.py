from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
c = (1 for x in [1])
d = (x for x in [1,2,3])
e = (x if x%2 == 0 else x+1 for x in [1,2,3])
f = (x if x%2 == 0 else x+1 for x in range(100000))
g = (x if x%2 == 0 else x+1 for x in range(10000000))

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(isinstance(d, GeneratorType))
print(isinstance(e, GeneratorType))
print(isinstance(f, GeneratorType))
print(isinstance(g, GeneratorType))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))
print(isinstance(d, FunctionType))
print(isinstance(e, FunctionType))
print(isinstance(f, FunctionType))
print
