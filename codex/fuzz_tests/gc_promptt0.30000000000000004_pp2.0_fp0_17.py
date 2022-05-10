import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a

refs = {id(a): weakref.ref(a),
        id(b): weakref.ref(b)}

del a, b
gc.collect()

for oid, ref in refs.items():
    obj = ref()
    if obj is not None:
        print(oid, 'still reachable')

# Test gc.get_referrers()

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a

refs = {id(a): weakref.ref(a),
        id(b): weakref.ref(b)}

del a, b
gc.collect()

for oid, ref in refs.items():
    obj = ref()
    if obj is not None:
        print(oid, 'still reachable by', gc.get_referrers(obj))

# Test gc.get_
