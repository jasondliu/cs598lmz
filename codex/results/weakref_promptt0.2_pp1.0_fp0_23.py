import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o2 = r()
print(o is o2)

del o
print(r())

del o2
print(r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print(p)
print(p.__class__)

o2 = p
print(o is o2)

del o
try:
    p.foo
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)
print(weakref.getweakrefcount(o))

p = weakref.proxy(o)
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()

o = C()
print(weakref.getweakrefs
