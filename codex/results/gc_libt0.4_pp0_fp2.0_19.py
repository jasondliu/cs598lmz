import gc, weakref

class C(object):
    pass

c = C()

# create a weak reference to c
r = weakref.ref(c)

# delete the original reference to c
del c

# the object is still alive, but the reference is dead
print r() is None

# create a new reference to the object
c = r()

# delete the weak reference
del r

# the object is still alive, but the reference is dead
print c is None

# the object is still alive, but the reference is dead
print gc.get_referrers(c) == []

# the object is dead
del c

print gc.get_referrers(c)
</code>

