import weakref
# Test weakref.ref factory for subclasses that implement a custom __hash__()
# method.


class Refhash(weakref.ref):

    def __hash__(self):
        return id(self)

    def __call__(self):
        return self


class CallHash(object):

    def __hash__(self):
        return id(self)


def f():
    pass
x = f

# A straightforward test would be
#
#     d = weakref.WeakKeyDictionary()
#     d[Refhash(x)] = 42
#
# since that triggers the assertion.  But because this is a regression test
# we have to be sure it fails even when the objects in question happen to
# have a valid __hash__() implementation, in case some "optimization" would
# circumvent the assertion.
#
# First, compute the hash of the (valid) object.

v = Refhash(x)
h = v.__hash__()

# Next, insert the object into a WeakValueDictionary with a valid key.
# (Note that this object *is not* callable, so
