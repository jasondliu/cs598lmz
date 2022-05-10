from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

b = (x for x in [1, 2, 3])
print(b)
print(type(b))

# print(b[1])

c = list(b)
print(c)

print(c[2])

# help(b)

print(isinstance(b, tuple))

print(FunctionType)

print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

print(isinstance([1], Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))
print(isinstance(b, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,
