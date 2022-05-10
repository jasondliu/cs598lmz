import weakref
# Test weakref.ref() for objects of dynamically allocated types.
class C(object):
    pass

def f():
    x = C()
    x.y = C()
    x.y.z = C()
    wr = weakref.ref(x.y.z)
