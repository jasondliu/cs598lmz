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

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)

del o
print(p)
