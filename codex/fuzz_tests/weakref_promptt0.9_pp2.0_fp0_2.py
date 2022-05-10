import weakref
# Test weakref.ref and weakref.proxy.

# First test with mutable object (a list object)

class C:
    mutable = [1, 2, 3]

obj = C()
obj_id = id(obj)
pref = weakref.ref(obj)
wproxy = weakref.proxy(obj)
proxy_id = id(wproxy)
if repr(wproxy).find("[1, 2, 3]") < 0:
    raise RuntimeError("proxy did not print object's repr")
if wproxy.mutable[2] != 3:
    raise RuntimeError("proxy didn't behave like object")
del obj
del wproxy
# Cannot assert that pref() is None, since a gc run triggered by
# this test would sweep the list.
# See Weakref gc interaction in the docs.
# However, I can assert that proxy is dead.
try:
    print(wproxy.mutable)
    raise RuntimeError("weak proxy did not die")
except ReferenceError:
    pass
# Now check that it also works for immutable objects
obj = C()
obj.mutable
