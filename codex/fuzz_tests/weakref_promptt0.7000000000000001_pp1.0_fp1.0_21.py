import weakref
# Test weakref.ref:
r = weakref.ref(old_object)
r() is old_object
r() is not None

def callback(reference):
    print 'callback(', reference, ')'

r = weakref.ref(old_object, callback)

# Test weakref.proxy
p = weakref.proxy(old_object)
p
p.attribute
p.method()

del old_object
r() is None
r() is None

try:
    p.attribute
except ReferenceError:
    print 'Caught exception!'
