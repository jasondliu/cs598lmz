import gc, weakref

class X(object):
    def __del__(self):
        print "dead"

gc.enable()

x = X()
r = weakref.ref(x)

print r() is x

del x

print r() is None
</code>

