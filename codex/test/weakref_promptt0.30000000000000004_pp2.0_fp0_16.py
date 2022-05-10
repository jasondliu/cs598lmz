import weakref
# Test weakref.ref
import gc

class C:
    pass

o = C()
r = weakref.ref(o)

print(r())
print(r() is o)
print(r() is None)

o2 = C()
r2 = weakref.ref(o2)

print(r2() is o2)

del o2
print(gc.collect())
print(r2() is None)

# Test weakref.proxy

class D:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

l = [D(i) for i in range(10)]
d = dict([(str(i), D(i)) for i in range(10)])

p = weakref.proxy(l)
print(p)
print(p[2])

p = weakref.proxy(d)
print(p)
print(p["2"])

l[2].value = 12
print(p[2])

d
