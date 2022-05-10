import weakref
# Test weakref.ref is working.
a = weakref.ref(long())

assertNull(a)

b = weakref.ref(long(2))

assertNotNull(b)

