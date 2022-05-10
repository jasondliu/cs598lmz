import weakref
# Test weakref.ref(obj)

class C:
    pass

c = C()
r = weakref.ref(c)
assert r() is c

# Test weakref.ref(obj, callback)

class C:
    pass

c = C()
l = []
def callback(arg):
    l.append(arg)
r = weakref.ref(c, callback)
assert r() is c
del c
assert l == [r]

# Test weakref.proxy(obj)

class C:
    pass

c = C()
p = weakref.proxy(c)
assert p is c

# Test weakref.proxy(obj, callback)

class C:
    pass

c = C()
l = []
def callback(arg):
    l.append(arg)
p = weakref.proxy(c, callback)
assert p is c
del c
assert l == [p]

# Test weakref.getweakrefcount(obj)

class C:
    pass

c = C()
assert weakref.getweakrefcount
