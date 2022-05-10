from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x: x for x in [1]}
e = lambda x: x
f = FunctionType(lambda x: x, {})


def g(x):
    return x


h = type(g)
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h))
print(type(a) is type(b), type(b) is type(c), type(c) is type(d))
print(type(d) is type(e), type(e) is type(f), type(f) is type(g), type(g) is type(h))


def f1(a):
    return a


def f2(a, b):
    return a + b


def f3(a, b, c):
    return a + b + c


print(f1.__code__.co_argcount)
print(f2.__code__.co_arg
