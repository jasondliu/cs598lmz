import weakref
# Test weakref.ref()

import weakref

class C:
    pass

# Weak reference to an instance of the class.
c = C()
r = weakref.ref(c)
