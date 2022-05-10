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
