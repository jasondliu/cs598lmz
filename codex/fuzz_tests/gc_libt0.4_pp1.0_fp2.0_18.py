import gc, weakref

class C(object):
    pass

c = C()

w = weakref.ref(c)

print w() is c

del c

gc.collect()

print w() is None
</code>

