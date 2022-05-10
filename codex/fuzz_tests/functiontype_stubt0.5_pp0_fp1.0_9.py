from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(type(lambda x: x))
print(type(FunctionType))
print(type(abs))
print(type(a.__iter__))
print(type(a.__next__))
print(type(iter))

def fn():
    pass

class A:
    pass

print(type(fn))
print(type(A))
print(type(A()))

class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        return type.__new__(cls, name, bases, attrs)

class Foo(object, metaclass=MyMeta):
    bar = True
    def __init__(self):
        pass

print(type(Foo))
print(type(Foo()))

class MyList(list):
    def __init__(self, *args):
        super().__init__(
