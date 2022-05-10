import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

o2 = C()
r2 = weakref.ref(o2, lambda x: print('callback'))
assert r2() is o2

del o2
gc.collect()

assert r2() is None

# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)
assert p is o

o2 = C()
p2 = weakref.proxy(o2, lambda x: print('callback'))
assert p2 is o2

del o2
gc.collect()

try:
    p2.attr
except ReferenceError:
    print('ReferenceError')

# Test weakref.getweakrefcount()

class C:
    pass

o = C()
assert weakref.getweakrefcount(o) == 0

r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1

