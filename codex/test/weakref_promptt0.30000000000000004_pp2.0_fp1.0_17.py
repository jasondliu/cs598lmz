import weakref
# Test weakref.ref() and weakref.proxy()

import weakref

class C(object):
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

