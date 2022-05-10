import weakref
# Test weakref.ref for C-defined classes.


class A(object):
    pass


class B(object):
    pass


class Foo(object):
    """A class that has finalizers on its instances."""

    def __init__(self):
        self.counter = 0

    def __del__(self):
        self.counter += 1


class Bar(object):
    """A class that has finalizers on its instances, but
    which does not inherit from object.
    """

    def __init__(self):
        self.counter = 0

    def __del__(self):
        self.counter += 1


FooType = type(Foo)
BarType = type(Bar)

# create and destroy some instances to be sure the types
# have been initialized
for c in (A, B, Foo, FooType, Bar, BarType):
    x = c()
    x = None
print('done creating/destroying instances')

# create a weakref to each instance, and then let it die.
# The ref should call the finalizer when the instance dies.
# We
