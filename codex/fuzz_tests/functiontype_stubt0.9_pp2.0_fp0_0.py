from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
c = a
print(a is c)
print(a is not b)

print(bool(0))
print(bool(()))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(''))


def mul(x, y):
    return x + y

d = FunctionType
print(type(type))
