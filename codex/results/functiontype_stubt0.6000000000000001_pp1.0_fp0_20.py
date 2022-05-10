from types import FunctionType
a = (x for x in [1])
b = (x for x in [1, 2])
c = (x for x in [1, 2, 3])
d = (x for x in [1, 2, 3, 4])

print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(isinstance(d, GeneratorType))

print(a)
print(b)
print(c)
print(d)

print(next(a))
print(next(b))
print(next(c))
print(next(d))

print(next(b))
print(next(c))
print(next(d))

print(next(c))
print(next(d))

print(next(d))

print(a)
print(b)
print(c)
print(d)
