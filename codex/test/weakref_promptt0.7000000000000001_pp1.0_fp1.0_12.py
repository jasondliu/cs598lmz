import weakref
# Test weakref.ref's metaclass by inheriting from a built-in type

class MyRef(weakref.ref):

    def __init__(self, object, callback=None, **kwds):
        self.__dict__ = kwds
        weakref.ref.__init__(self, object, callback)

    def __repr__(self):
        return 'MyRef(%s)' % (weakref.ref.__repr__(self),)

    def __call__(self):
        return 'MyRef(%s)' % (weakref.ref.__call__(self),)

    # __str__ is inherited from the base class, but we need to
    # override it for the doctest to work
    def __str__(self):
        return 'MyRef(%s)' % (weakref.ref.__str__(self),)

class Foo(int): pass

def main():
    o = Foo(42)
    f = MyRef(o)
    f.hello = 'world'
