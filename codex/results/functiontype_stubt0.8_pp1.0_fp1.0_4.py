from types import FunctionType
a = (x for x in [1])

print(type(a))

def foo():
    pass
print(type(foo))
print(type(lambda x: x + 10))
print(type((x for x in range(10))))
print(type(foo.__code__))

print(type(foo.__code__.co_code))
print(type(type))

class A:
    pass

print(type(A))


class Meta(type):
    pass

class A(metaclass=Meta):
    pass

print(type(A))
print(type(Meta))

print(type(Meta))
print(Meta.__class__)
print(type(Meta.__class__))


def foo(x):
    pass

print(foo.__class__)
print(type(foo.__class__))


class A:
    pass

a = A()

print(foo.__class__)
print(type(foo.__class__))

print(isinstance(a, A))

print(foo.__class__)

print
