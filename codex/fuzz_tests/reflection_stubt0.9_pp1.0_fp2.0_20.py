fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


# classmethods
class A:
    @classmethod
    def foo(cls):
        print(cls.__class__)
A.foo()
a = A()
a.foo()

# Adding a method
def foo(self):
    print("foo")
A.foo2 = foo
A.foo2()
a.foo2()

# Descriptors
class Descr:
    def __get__(self, obj, objtype):
        print("get", self, obj, objtype)
    def __set__(self, obj, value):
        print("set", self, obj, value)
    def __delete__(self, obj):
        print("del", self, obj)
class A:
    x = Descr()
a = A()
a.x
a.x = 3
del a.x

# Slots
class A:
    __slots__ = ['x']
a = A()
a.x = 3

class A:
    __slots__ = ['name', 'age']

