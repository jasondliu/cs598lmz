import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r())

del o
print(r())

o2 = C()
r2 = weakref.ref(o2)
print(r2())
print(r())

o = o2
r3 = weakref.ref(o)
print(r3())
print(r2())

del o2
print(r3())
print(r2())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)

del o

try:
    print(p)
except ReferenceError:
    print('ReferenceError')

# Test weakref.getweakrefcount()

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)
print(weakref.getweakrefcount(o))

p = weakref.proxy(o)
print(weakref.getweakrefcount(o))

del r

