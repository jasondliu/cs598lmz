from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(a == b)
print(a is b)
print(False and True)
print(1 and 1)
print(1 is True)
print(True is True)
print(True is 1)


def a():
    print(1)


def b():
    print(2)


c = a or b
c()
print(type(c))
print(isinstance(c, FunctionType))


class A:
    pass


print(isinstance(A, FunctionType))
A()

a()
