import weakref
# Test weakref.ref(object)
# Test weakref.ref(object, callback)
# Test weakref.ref(object, callback, key)
# Test weakref.proxy(object)
# Test weakref.proxy(object, callback)
# Test weakref.proxy(object, callback, key)

# Test weakref.getweakrefcount(object)
# Test weakref.getweakrefs(object)

# Test that weakrefs to ints are allowed (issue #1202)
import weakref
for i in range(100):
    weakref.ref(i)

# Test that a weakref callback gets a reference to the weakly referenced object
# as well as a reference to the referent, and that the two values are the same.
# (issue #1113)
import weakref

class Foo:
    pass

def callback(ref, obj):
    assert ref() is obj

foo = Foo()
foo_ref = weakref.ref(foo, callback)
# Create a new reference to foo so that it is not destroyed immediately.
foo2 = foo
del foo

import weak
