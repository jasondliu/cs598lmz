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
else:
    print 'No exception raised for non-weakable object'

# Test weakref.ref() on a weak ref object.
try:
    r = weakref.ref(r)
except TypeError:
    pass
else:
    print 'No exception raised for weak reference object'

w = _weakref.ref(x)
try:
    r = weakref.ref(w)
except TypeError:
    pass
else:
    print 'No exception raised for weak reference object'
