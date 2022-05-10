import weakref
# Test weakref.ref(C)(x) in a metaclass, where C is a subclass of the metaclass.

class Meta(type):
    def __new__(meta, name, bases, ns):
        ns['x'] = 42
        return type.__new__(meta, name, bases, ns)


class C(metaclass=Meta):
    pass


r = weakref.ref(C)
# Ensure that the weakref is alive
assert r() is not None
# Ensure that the weakref is to the correct class
assert r() is C
# Ensure that the weakref has the correct attribute
assert r().x == 42

# Ensure that the weakref is alive
assert r() is not None
# Ensure that the weakref is to the correct class
assert r() is C
# Ensure that the weakref has the correct attribute
assert r().x == 42
# Ensure that the weakref is alive
assert r() is not None
# Ensure that the weakref is to the correct class
assert r() is C
# Ensure that the weakref has the correct attribute
assert r().x == 42
# Ensure that
