from types import FunctionType
a = (x for x in [1])
print(type(a))
print(dir(a))

b = type(a)
print(type(b))
print(dir(b))

print(isinstance(a, b))

print(isinstance(b, type))

print(type(a) is FunctionType)

# __class__
print(a.__class__)

# __subclass__
print(list.__subclasses__())

# __init_subclass__
class A(object):
    pass

class B(A):
    pass

print(A.__subclasses__())
print(B.__subclasses__())

class A(object):
    def __init_subclass__(cls):
        print("A init subclass")
        super().__init_subclass__()

class B(A):
    pass

class C(A):
    pass

print(A.__subclasses__())

class A(object):
    def __init_subclass__(cls):
        print("A init subclass")
        super().__init
