import weakref
# Test weakref.ref(self, self.on_delete)
#
# Tests the lifetime of a reference to a weakref.ref
# helper object.
#
# This script checks that the reference on "r" is
# None when a weakrefable object is deleted.
# See https://bugs.python.org/issue18780
class WeakRefTest(object):
    def __init__(self, i):
        self.i = i

    def on_delete(self, *args):
        print('on_delete called')
        r.append(1)


def g():
    r = []
    for i in range(20):
        print('creating {0}'.format(i))
        x = WeakRefTest(i)
        wr = weakref.ref(x, 
