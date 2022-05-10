import weakref
# Test weakref.ref() behavior for operations on the proxy object.
import weakref
import gc

class Foo(object):
    pass

def callback(r):
    print 'Callback called'
    f = r()
    print 'f is', f
    del f


f = Foo()
r = weakref.ref(f, callback)
gc.collect()
print 'f is', f
print 'r is', r
del f
print 'f is now', f
print 'r is now', r
