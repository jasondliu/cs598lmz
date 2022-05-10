import weakref
# Test weakref.ref() on methods
def callback(r):
    raise ValueError

class Foo:
    def f(self):
        pass

r = weakref.ref(Foo().f, callback)
del Foo
# Test weakref.ref() on objects with a custom __hash__
class Foo(object):
    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return self is other

f = Foo()
r = weakref.ref(f)
del f
# Test weakref.ref() on objects with a custom __hash__
class Foo(object):
    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return self is other

f = Foo()
r = weakref.ref(f)
del f
# Test weakref.ref() on objects with a custom __hash__
class Foo(object):
    def __init__(self, obj):
        self.obj = obj

    def __hash__(self):
        return id(self.obj)


