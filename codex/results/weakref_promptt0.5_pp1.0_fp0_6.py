import weakref
# Test weakref.ref(x) == weakref.ref(x)

# Test the case where the referent is the same object.

class X:
    pass

x = X()

r = weakref.ref(x)
r2 = weakref.ref(x)

assert r is r2

# Test the case where the referent is a different object, but
# __eq__ says they are equal.

class X:
    def __eq__(self, other):
        return True

x = X()
y = X()

r = weakref.ref(x)
r2 = weakref.ref(y)

assert r is r2
