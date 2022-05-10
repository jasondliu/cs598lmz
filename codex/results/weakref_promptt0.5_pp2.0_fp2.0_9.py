import weakref
# Test weakref.ref() with a class that has a __hash__ method
# with a bug.

class C(object):
    def __hash__(self):
        return 0

c = C()
r = weakref.ref(c)
assert r() is c
assert hash(r) == 0

# Now break __hash__.
del C.__hash__
try:
    hash(r)
except TypeError:
    pass
else:
    print("Expected TypeError")
