import weakref
# Test weakref.ref:
r = weakref.ref(42)
r2 = weakref.ref(r)
r() == r and r2() == r
r2() is r
r()
r2()

# Test weakref.WeakValueDictionary:
import gc
d = weakref.WeakValueDictionary()
o = C()
d[1] = o
d[2] = o
ret = d[1], d[2]
o.x = "dead"
gc.collect()
list(d.items())
tuple(ret) == (o, o)
tuple(d.items()) == ()

# Test weakref.WeakKeyDictionary:
d = weakref.WeakKeyDictionary()
o = C()
d[o] = 1
o.x = "dead"
gc.collect()
list(d.items())
list(d.items()) == []

# Test weakref.finalize:
objs = []
for i in range(100):
    obj = C()
    objs.append(obj)
    weakref.finalize(
