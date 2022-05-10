import weakref
# Test weakref.ref() being garbage collected.

class A:
    pass


class B:
    pass
a = A()

# Not collected.
wr = weakref.ref(a)
wr() is a

# Collected with finalizer.
