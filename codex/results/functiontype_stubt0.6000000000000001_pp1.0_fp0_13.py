from types import FunctionType
a = (x for x in [1])
print(a)

print(isinstance(a, Iterator))

print(isinstance(a, Iterable))

print(a is Iterable)

print(isinstance(a, FunctionType))


def g():
    yield 1


print(isinstance(g(), Iterator))

print(isinstance(g(), Generator))
