import weakref
# Test weakref.ref() with a class-based object, which
# has a __weakref__ attribute.
import weakref

class C(object):
    pass

c = C()
r = weakref.ref(c)
c.__weakref__ is r
# Make sure we can create a weak reference to a weakref object.
import weakref

class C(object):
    pass

c = C()
r = weakref.ref(c)
r2 = weakref.ref(r)
r2() is r
r2() is c
r2 is r
# Make sure we can create a weak reference to an object with a weakref.
import weakref

class C(object):
    pass

c = C()
r = weakref.ref(c)
c.r = r
r2 = weakref.ref(c.r)
r2 is r
r2() is r
r2() is c
# Make sure we can create a weak reference to an object with a weakref.
import weakref

class C(object):
    pass

c = C()

