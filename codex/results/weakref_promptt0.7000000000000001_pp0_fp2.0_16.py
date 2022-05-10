import weakref
# Test weakref.ref objects

import weakref
import gc

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda u: print("callback"))

print(r2)
print(r2())

del o2
gc.collect()

del o
gc.collect()
print(r())
print(r2())

# Test weakref.proxy objects

import weakref
import gc

class C:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "C(%r)" % self.x

o = C(42)
p = weakref.proxy(o)

print(p)
print(p.x)

o2 = C(1)
p2 = weakref.proxy(o2, lambda u: print("callback"))

print(p2)
print(p2.x)

o
