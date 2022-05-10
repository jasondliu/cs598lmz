import weakref
# Test weakref.ref making a # ref to a class instance (it creates a weakref,
# but causes a segfault or other crash at destruction time)
import _weakref


# Test basic weakref behaviour
class C:
    pass


obj = C()
w = weakref.ref(obj)
assert w() is obj
obj = None
C = None
# assert that the weakref's hash is the same as the hash of the
# underlying object
print(hash(w), hash(w()))
import gc
gc.collect()
assert w() is None

# Test basic proxy behaviour
class C:
    pass


obj = C()
w = weakref.proxy(obj)
assert w is obj
obj = None
C = None
# On next line, assert that the weakref's hash is the same as the
# hash of the underlying object
print(hash(w), hash(w()))
import gc
gc.collect()
try:
    w.some_method_that_does_not_exist()
except ReferenceError:
    pass
else:
    raise MyError, '
