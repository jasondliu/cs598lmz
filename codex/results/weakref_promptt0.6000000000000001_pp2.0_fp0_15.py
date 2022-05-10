import weakref
# Test weakref.ref
class C:
    pass
o = C()
r = weakref.ref(o)
print(r)
print(r())
print(o)

# Test weakref.proxy
class D:
    pass
p = D()
x = weakref.proxy(p)
print(x)

# Test weakref.getweakrefcount
print(weakref.getweakrefcount(p))
print(weakref.getweakrefcount(p))
print(weakref.getweakrefcount(o))
