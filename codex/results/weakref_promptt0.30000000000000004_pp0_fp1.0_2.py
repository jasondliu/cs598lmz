import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

del o
print(r)
print(r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print(p)
print(p.x)

del o
print(p)
print(p.x)
