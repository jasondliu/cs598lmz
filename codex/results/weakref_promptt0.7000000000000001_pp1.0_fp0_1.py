import weakref
# Test weakref.ref() with a weakref.KeyedRef instance.
import weakref
# Initialize objects to be tracked
o = C()
d = {}
# Create weak references
r = weakref.ref(o)
k = weakref.KeyedRef(o, lambda o: id(o))
# Check that they can be called
r()
k()
# Check that they are equal
r == k
# Check that they are unequal to other objects
r != o
r != k()
r != d
# Check that the keyed ref is hashed properly
hash(k)
# Check that the weak references can be cleared
r2 = weakref.ref(o)
k2 = weakref.KeyedRef(o, lambda o: id(o))
r2 is r
k2 == k
# Clear the references
r2 = None
k2 = None
# Check that they have been cleared
r2 is None
k2 is None
# Check that they can be used in a dictionary
d[r] = 5
d[k] = 'hello'
d[r]
d[k]
# Check
