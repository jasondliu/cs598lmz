from types import FunctionType
a = (x for x in [1])
b = (x for x in [1, 2, 3])
c = (x for x in [1, 2, 3, 4, 5])
d = (x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9])

def my_map(func, *iterables):
    for iterable in iterables:
        for x in iterable:
            yield func(x)

for x in my_map(lambda x: x + 1, a):
    print(x)

for x in my_map(lambda x, y: x + y, b, c):
    print(x)

for x in my_map(lambda x, y, z: x + y + z, b, c, d):
    print(x)

print("\n")

# Fora da correção

def my_map2(function, *iterables):
    if not callable(function):
        raise TypeError("argument 1 must be a function")
    for iterable in iterables:
        for x in iterable:

