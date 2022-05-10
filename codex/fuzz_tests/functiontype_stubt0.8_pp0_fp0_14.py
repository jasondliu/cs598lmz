from types import FunctionType
a = (x for x in [1])
b = (x for x in range(3))


def fn():
    x = 1
    y = 2
    return x + y


def fn1(x, y):
    return x + y


print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(fn, FunctionType))
print(isinstance(fn1, FunctionType))
