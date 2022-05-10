import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print(r())
print(r() is o)
print(r() is None)

del o
print(r() is None)

# Test weakref.proxy()

class D:
    pass

o = D()
p = weakref.proxy(o)

print(p)
print(p is o)

del o
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

class E:
    pass

o = E()
r1 = weakref.ref(o)
r2 = weakref.ref(o)

print(weakref.getweakrefcount(o))
print(weakref.getweakrefcount(o) == 2)

# Test weakref.getweakrefs()

class F:
    pass

o = F()
r1 = weakref.ref(o)
