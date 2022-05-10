import weakref
# Test weakref.ref

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(o)

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())
print(o2)

print(r is r2)
print(r() is r2())

print(r is r)
print(r() is r())

print(r2 is r2)
print(r2() is r2())

# Test weakref.proxy

o = C()
p = weakref.proxy(o)
print(p)
print(p.__class__)

try:
    weakref.proxy(42)
except TypeError:
    print("TypeError")

try:
    weakref.proxy(None)
except TypeError:
    print("TypeError")

# Test weakref.getweakrefcount

o = C()
print(weakref.getweakrefcount(o))
r = weakref.ref
