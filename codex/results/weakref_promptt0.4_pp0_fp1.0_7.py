import weakref
# Test weakref.ref() and weakref.proxy()

class C:
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print(r(), r() is o)
print(p, p is o)

o2 = r()
print(o2 is o)

o3 = p
print(o3 is o)

del o
del o3

print(r() is None)
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount() and weakref.getweakrefs()

a = C()
b = C()

print(weakref.getweakrefcount(a), weakref.getweakrefcount(b))

r1 = weakref.ref(a)
print(weakref.getweakrefcount(a), weakref.getweakrefcount(b))

r2 = weakref.ref(a)
print(weakref.getweakrefcount(a), weakref.getweakrefcount(b))

