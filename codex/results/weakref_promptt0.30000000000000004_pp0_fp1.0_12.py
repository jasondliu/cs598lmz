import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r())
del o
print(r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p.foo)
del o
print(p.foo)
