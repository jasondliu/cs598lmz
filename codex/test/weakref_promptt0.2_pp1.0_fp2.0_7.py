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

def callback(r):
    global called
    called = True

called = False
r = weakref.ref(c, callback)
del c
assert called

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

def callback(r):
    global called
    called = True

called = False
p = weakref.proxy(c, callback)
del c
assert called

# Test weakref.getweakrefcount(obj)

class C:
    pass

c = C()
assert weakref.getweakrefcount(c) == 0
