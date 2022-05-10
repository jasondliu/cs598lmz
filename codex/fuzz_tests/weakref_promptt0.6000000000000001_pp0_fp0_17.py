import weakref
# Test weakref.ref()

class C:
    pass

c = C()
r = weakref.ref(c)
if r() is not c:
    raise TestFailed, "weakref.ref(c) did not return c"

# Test weakref.getweakrefcount()
if weakref.getweakrefcount(c) != 1:
    raise TestFailed, "wrong weakref count for c"

if weakref.getweakrefcount(c) != 1:
    raise TestFailed, "wrong weakref count for c"

# Test weakref.getweakrefs()
if r not in weakref.getweakrefs(c):
    raise TestFailed, "c was not found in weakrefs"

# Test weakref.proxy()
p = weakref.proxy(c)
if p.__class__ is not weakref.ProxyType:
    raise TestFailed, "p.__class__ is not weakref.ProxyType"

if p is not c:
    raise TestFailed, "p is not c"

# Test weakref.proxy()
