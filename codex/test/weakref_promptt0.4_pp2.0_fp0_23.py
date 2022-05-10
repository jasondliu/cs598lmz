import weakref
# Test weakref.ref()
import sys

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(sys.getrefcount(o))
del o
gc.collect()
print(r())
print(r() is None)

# Test weakref.proxy()
class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)
print(p.x)
del o
try:
    print(p.x)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount() and weakref.getweakrefs()
class C:
    pass

o = C()
d = weakref.WeakKeyDictionary()
d[o] = 1
l = [o]
print(weakref.getweakrefcount(o))
print(weakref.getweakrefs(o))
del o
gc.collect()
print(d)
print(l)

# Test weakref.finalize()
