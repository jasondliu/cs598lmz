import weakref
# Test weakref.ref
class C:
    pass
o = C()
r = weakref.ref(o)
print(r)
o2 = r()
print(o2 is o)
o3 = C()
r2 = weakref.ref(o3)
print(r2)
print(r2() is o3)
o3 = None
print(r2())
print(r2() is None)
print(r2() is None)
# Test __repr__ on weakrefs
class D:
    pass
o = D()
r = weakref.ref(o)
print(str(r))
print(repr(r))
print(r)
o = None
print(str(r))
print(repr(r))
print(r)
# Test weakref.proxy
o = C()
p = weakref.proxy(o)
print(p.__class__)
print(p.__class__ is weakref.ProxyType)
print(p)
print(p is o)
print(p == o)
print(p != o)
print
