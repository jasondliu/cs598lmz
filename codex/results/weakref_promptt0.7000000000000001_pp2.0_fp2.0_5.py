import weakref
# Test weakref.ref(x)
class C:
    pass
x = C()
z = weakref.ref(x)
# Verify that z() returns the original reference
assert z() is x
# Verify that z() still returns the original reference after the original
# reference is deleted
del x
assert z() is not None
# Verify that z() returns None after the original reference is reclaimed
import gc
gc.collect()
assert z() is None
class C:
    pass
x = C()
w = weakref.ref(x)
# Verify that repr(w) works
repr(w)
# Verify that str(w) works
str(w)
# Verify that w() works
w()
# Verify that w() still works after the original reference is deleted
del x
assert w() is not None
# Verify that w() returns None after the original reference is reclaimed
gc.collect()
assert w() is None
class C:
    pass
x = C()
z = weakref.ref(x)
# Verify that callable(z) is true
assert callable(z)
# Verify that bool(
