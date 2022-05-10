import weakref
# Test weakref.ref() on a non-weak object.
import _weakref

class C(object):
    pass

x = C()
try:
    r = weakref.ref(x)
except TypeError:
    pass
