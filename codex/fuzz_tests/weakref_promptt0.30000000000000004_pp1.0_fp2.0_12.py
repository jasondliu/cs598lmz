import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o2 = r()
print(o2)
print(o is o2)

o3 = C()
r2 = weakref.ref(o3)
print(r2)
print(r2())

print(r is r2)
print(r() is r2())

# Test weakref.proxy()

class D:
    pass

o = D()
p = weakref.proxy(o)

print(p)
print(p.__class__)

o.attr = 42
print(p.attr)

del o
try:
    print(p.attr)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

class E:
    pass

o = E()
d = weakref.WeakKeyDictionary()
d[o] = 42

print(weakref.getweakrefcount(o))


