from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x:x for x in [1]}

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))
print(isinstance(d, FunctionType))

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(isinstance(d, GeneratorType))

print(isinstance(a, IteratorType))
print(isinstance(b, IteratorType))
print(isinstance(c, IteratorType))
print(isinstance(d, IteratorType))

print(isinstance(a, IterableType))
print(isinstance(b, IterableType))
print(isinstance(c, IterableType))
print(isinstance(d, IterableType))

print
