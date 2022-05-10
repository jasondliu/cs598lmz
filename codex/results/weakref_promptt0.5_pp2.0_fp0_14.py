import weakref
# Test weakref.ref() on a class

import weakref

class C:
    pass

c = C()
r = weakref.ref(c)
print(r(), c)
del c
print(r())
