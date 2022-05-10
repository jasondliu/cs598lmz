import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
print(r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)

del o
try:
    print(p)
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
r = weakref.ref(o)
p = weakref.proxy(o)
print(weakref.getweakrefs(o))

# Test weakref.finalize()

o = C()
r = weakref.ref(o)
print
