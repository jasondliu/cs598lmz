from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])


def g(x, y, z):
    return x+y+z

print(g(*a))
print(g(*b))
print(g(*c))

print(g(a, b, c))

print(g(*(a, b, c)))

print(g(a=a, y=b, z=c))

print(g(a, b, c))

print(g(a, y=b, z=c))

print(g(a, y=b, c))

print(g(a, b, z=c))

print(g(a, b, c))

print(g(a, b, c))

print(g(a, b, c))

print(g(a, b, c))

print(g(a, b, c))


def g(x, y, z):
    return x+y+z

print(g(a, b, c))


