import weakref
# Test weakref.ref() on a class.
class Foo:
    pass
r = weakref.ref(Foo)
r()

r() is Foo

r = weakref.ref(Foo())
r()

r() is Foo()

# Test weakref.ref() on an instance.
class Foo:
    def __del__(self):
        pass

class Bar:
    pass

def getFooRef():
    return weakref.ref(Foo())

r = getFooRef()

# We need to make sure that 'Foo' instance is not garbage collected
# before we can test its __del__ method.
# Sometime, we need a few more invocations of getFooRef() to reach
# this objective, so we repeat the loop a few times.
for i in xrange(10):
    r.__del__ = unittest.mock.Mock()
    r = getFooRef()

del r
# This should run the __del__ method of the 'Foo' instance.
gc.collect()
