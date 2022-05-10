import weakref
# Test weakref.ref() and weakref.proxy()

class C:
    pass

# Create a normal reference
c = C()
r = weakref.ref(c)
assert r() is c

# Create a proxy
p = weakref.proxy(c)
assert p is c

# Proxies are weakrefs, too
assert isinstance(p, weakref.ref)

# Create a weak reference to a proxy
r = weakref.ref(p)
assert r() is c

# Create a proxy to a proxy
p2 = weakref.proxy(p)
assert p2 is c

# Create a weak reference to a proxy to a proxy
r = weakref.ref(p2)
assert r() is c

# Create a proxy to a weak reference
p = weakref.proxy(r)
assert p is c

# Create a weak reference to a proxy to a weak reference
r2 = weakref.ref(p)
assert r2() is c

# Create a proxy to a proxy to a weak reference
p2 = weakref.proxy(p)
assert p2
