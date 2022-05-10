from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))

print(dir(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

# for x in a:
#     print(x)

print(a.__next__())
print(next(a))

print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
