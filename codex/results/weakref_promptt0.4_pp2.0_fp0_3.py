import weakref
# Test weakref.ref(object)

def f(x):
    return weakref.ref(x)

class C:
    pass

c = C()
r = f(c)
print repr(r)

# Test weakref.ref(object, callback)

class C:
    pass

def callback(r):
    print "callback:", r

c = C()
r = weakref.ref(c, callback)
print repr(r)

del c

# Test weakref.proxy(object)

class C:
    pass

c = C()
p = weakref.proxy(c)
print repr(p)
print p.__class__

# Test weakref.proxy(object, callback)

class C:
    pass

def callback(r):
    print "callback:", r

c = C()
p = weakref.proxy(c, callback)
print repr(p)
print p.__class__

del c

# Test weakref.getweakrefcount()

class C:
    pass

c = C
