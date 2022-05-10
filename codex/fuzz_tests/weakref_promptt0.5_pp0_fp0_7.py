import weakref
# Test weakref.ref

class C:
    pass

def foo(x, y):
    print("foo", x, y)

# ref(C)
r = weakref.ref(C)
assert r() is C

# ref(C(), foo)
r = weakref.ref(C(), foo)
assert r() is None

# ref(C(), None)
r = weakref.ref(C(), None)
assert r() is None

# ref(C(), 2)
try:
    weakref.ref(C(), 2)
except TypeError:
    pass
else:
    raise Exception("Should have raised TypeError")

# ref(C(), (1, 2, 3))
try:
    weakref.ref(C(), (1, 2, 3))
except TypeError:
    pass
else:
    raise Exception("Should have raised TypeError")
