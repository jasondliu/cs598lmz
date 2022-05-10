import weakref
# Test weakref.ref() with a proxy object.
class Foo(object):
    pass


class Bar(object):
    pass


class FooProxy(object):
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


a = Foo()
b = FooProxy(a)
r = weakref.ref(b)
print(r().obj is a)
del b
print(r() is None)
a = Bar()
b = FooProxy(a)
r = weakref.ref(b)
print(r().obj is a)
del b
print(r() is None)
# Test weakref.ref() with a new-style class.
class Foo(object):
    pass


a = Foo()
r = weakref.ref(a)
print(r() is a)
del a
print(r() is None)
# Test weakref.ref() with an instance of a classic class.
class Foo:
    pass


a = Foo()
