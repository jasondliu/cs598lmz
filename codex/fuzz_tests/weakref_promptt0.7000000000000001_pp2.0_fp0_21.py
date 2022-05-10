import weakref
# Test weakref.ref()
import gc

# The class used for testing weak references.
class MyClass:
    pass

def callback(reference):
    print 'callback(', reference, ')'

# Create some objects
obj = MyClass()
d = weakref.WeakValueDictionary()
d['primary'] = obj
r = weakref.ref(obj, callback)

print 'd["primary"] =', d['primary']
print 'r() =', r()

# Set 'obj' to None, and watch the weak reference invoke the
# callback.
print 'setting obj = None'
obj = None
print 'd["primary"] =', d['primary']
print 'd["primary"] is None:', d['primary'] is None
print 'r() returns None:', r() is None

# Clear the references held by the gc module before running the test, to
# make sure the test does not fail due to the garbage collector having
# previously collected the object.
gc.collect()

# Verify that the weak references have been cleared.  Note that we
# can't test r() is None: 
