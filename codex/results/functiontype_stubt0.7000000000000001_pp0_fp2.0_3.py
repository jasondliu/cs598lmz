from types import FunctionType
a = (x for x in [1])
print(type(a))

b = (x for x in [2])
print(type(b))

print(type(lambda x:x))
print(type(FunctionType))

print(type(()))
print(type([]))
print(type({}))
# print(type(set()))
print(type('123'))
print(type(b'123'))
print(type(123))
print(type(None))
print(type(Ellipsis))
print(type(x for x in range(10)))

print(dir(type))
print(type.__dict__)
print(type.__class__)
print(type.__bases__)
print(type.__mro__)
print(type.__subclasses__)
print(type.__str__)
print(type.__new__(type))


class X(object):
    a = 1

print(X.__dict__)
print(X.__class__)
print(X.__bases__)
print(X.__mro
