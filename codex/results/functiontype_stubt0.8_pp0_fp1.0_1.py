from types import FunctionType
a = (x for x in [1])
type(a)

b = (x ** 2 for x in [1, 2, 3])
type(b)

# generator expressions can be nested
c = ((x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y)
type(c)

def f():
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                yield (x, y)

# generators can be used as function arguments
def f1(x):
    return x * x

print map(f1, [1, 2, 3])

a = [1, 2, 3]
b = (x ** 2 for x in a)
print list(b)

# generators can be used in list comprehensions
g = list(x ** 2 for x in [1, 2, 3])
print g

# generators are lazy, they are computed when needed
def f():
    print 'called f()'
    yield 1
    print 'called again f()'

