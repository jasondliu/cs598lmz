import weakref
# Test weakref.ref() with a class instance.

class C(object):
    pass

o = C()
r = weakref.ref(o)
print r() is o
print r() is None
del o
print r() is None

# Test weakref.ref() with a class instance and a callback.

class C(object):
    pass

o = C()
l = []
def callback(arg):
    l.append(arg)
r = weakref.ref(o, callback)
print r() is o
print r() is None
del o
print r() is None
print l == [o]

# Test weakref.ref() with a class instance and a callback that raises.

class C(object):
    pass

o = C()
l = []
def callback(arg):
    l.append(arg)
    raise ValueError
r = weakref.ref(o, callback)
print r() is o
print r() is None
del o
print r() is None
print l == [o]

# Test weakref.ref() with a class instance
