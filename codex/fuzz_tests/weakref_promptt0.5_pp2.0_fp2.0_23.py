import weakref
# Test weakref.ref()
import gc

class C:
    pass

o = C()
r = weakref.ref(o)

print(r())

o2 = r()
assert o is o2

o = None
gc.collect()

assert r() is None
assert r() is None

# Test weakref.proxy()
o = C()
p = weakref.proxy(o)

assert o is p

o = None
gc.collect()

try:
    p.foo
except ReferenceError:
    pass
else:
    raise Exception("should have raised ReferenceError")

# Test weakref.getweakrefcount()
o = C()
assert weakref.getweakrefcount(o) == 0

r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1

p = weakref.proxy(o)
assert weakref.getweakrefcount(o) == 2

o = None
gc.collect()
assert weakref.getweakrefcount(r()) == 0
assert weakref.getweakref
