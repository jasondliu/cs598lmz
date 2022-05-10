import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o = None
print(r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print(p)
print(p.foo)

o = None
try:
    print(p.foo)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)
r3 = weakref.ref(o)

print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()

o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)
r3 = weakref.ref(o)

print(weakref.getweakrefs(o))

# Test weakref.finalize()

o
