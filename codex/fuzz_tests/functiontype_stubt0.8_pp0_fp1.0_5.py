from types import FunctionType
a = (x for x in [1])
b = range(10)
c = 10


def f():
    print("hello")


print(type(a) == types.GeneratorType)
print(type(b) == types.GeneratorType)
print(type(c) == types.GeneratorType)
print(type(f) == FunctionType)
print(type(abs) == FunctionType)


def add(x, y, f):
    return f(x) + f(y)


print(add(5, -6, abs))


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
r1 = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r1))
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = list(map(str, a))
print(a)
# reduce(f,[x1,x2,
