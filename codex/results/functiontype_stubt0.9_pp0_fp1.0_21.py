from types import FunctionType
a = (x for x in [1])
print(type(a))
# print(repr(a))

# print(a(1))


class A(object):
    def __init__(self):
        self.b = (x for x in [2])


print(type(A().b))

print(type(A.__init__))

print(type(A.__new__))


class B(object):
    pass


print(isinstance(type(A), type(B)))


def foo():
    pass


print(type(foo))
print(isinstance(foo, FunctionType))

print(type(FunctionType))
print(type(object))
