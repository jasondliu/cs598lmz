import weakref
# Test weakref.ref()
for obj in [object(), {}, [], 1, 2.0]:
    print(weakref.ref(obj), obj)

for obj in [object(), {}, [], 1, 2.0]:
    r = weakref.ref(obj)
    print(bool(r), r, r(), obj)

# Test weakref.WeakValueDictionary()
d = weakref.WeakValueDictionary()
key = object()
obj = object()
d[key] = obj
print(d)

# Test gc on WeakValueDictionary
import gc
d = weakref.WeakValueDictionary()
key = object()
obj = object()
d[key] = obj
print(d)

print(gc.collect(), len(gc.garbage))
del obj
print(gc.collect(), len(gc.garbage))
d.clear()
print(d)

# Test weakref.WeakSet()
s = weakref.WeakSet()
obj = object()
s.add(obj)
print(s)

print(gc.collect(), len(
