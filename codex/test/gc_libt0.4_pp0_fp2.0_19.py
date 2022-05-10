import gc, weakref

class C(object):
    pass

c = C()

# create a weak reference to c
r = weakref.ref(c)

# delete the original reference to c
del c

# the object is still alive, but the reference is dead
