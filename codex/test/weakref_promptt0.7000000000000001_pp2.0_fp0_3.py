import weakref
# Test weakref.ref() with callbacks with a cyclic reference.  Issue #594.
#
import gc

class A(object):

    def __init__(self):
        self.b = B(self)

    def __del__(self):
        print('A.__del__')


class B(object):

    def __init__(self, a):
        self.a = a

    def __del__(self):
        print('B.__del__')


def callback(r):
    print('callback(%r)' % (r,))


def f():
    print('f()')
    a = A()
    a.b.a.b.a.b.a.b = None
    a.b.a.b.a.b.a = None
    a.b.a.b = None
    a.b.a = None
    r = weakref.ref(a, callback)
    a.b.a.b.a.b.a.b = None
    a.b.a.b.a.b.a = None

