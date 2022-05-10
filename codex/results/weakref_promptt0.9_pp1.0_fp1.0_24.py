import weakref
# Test weakref.ref for long lifetime cyclic objects.
# The original Python 2 version created a cycle with a lambda
# function, which is handled specially in the cyclic garbage
# collector (Py_LIMITED_API).  In Python 3, it is possible to
# create a simpler cycle that the Python implementation will not
# be able to break.

class C:
    def __init__(self, x=None):
        self.x = x

    def __repr__(self):
        return '%d' % self.x

def callback(r):
    print('callback(%r)' % r)

r = weakref.ref(C(), callback)
print(r())
