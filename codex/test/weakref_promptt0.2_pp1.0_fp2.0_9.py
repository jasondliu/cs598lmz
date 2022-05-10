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

del o
print(r())

del o2
print(r())

# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)

print(p)

o.foo = 1
print(p.foo)

del o
try:
    print(p.foo)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

class C:
    pass

o = C()

print(weakref.getweakrefcount(o))

r = weakref.ref(o)
print(weakref.getweakrefcount(o))

p = weakref.proxy(o)
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()

