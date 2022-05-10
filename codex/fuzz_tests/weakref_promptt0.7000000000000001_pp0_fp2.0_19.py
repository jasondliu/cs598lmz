import weakref
# Test weakref.ref(obj)
# Test weakref.ref(obj, callback)
# Test weakref.ref(obj, callback, key)

# Test weakref.proxy(obj)
# Test weakref.proxy(obj, callback)

class Foo(object):
    x = 0
    def __init__(self, x):
        self.x = x
    def display(self):
        print self.x

def debug_ref(obj):
    print "Reference to %r destroyed" % obj

def debug_proxy(obj):
    print "Proxy to %r destroyed" % obj


# Test weakref.ref(obj).
r = weakref.ref(Foo(1))
print r.x
r.x = 2
print r.x

# Test weakref.ref(obj, callback).
r = weakref.ref(Foo(1), debug_ref)
print r.x
r.x = 2
print r.x

# Test weakref.ref(obj, callback, key).
r = weakref.ref(Foo(1), debug_ref,
