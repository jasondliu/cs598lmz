import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()

import sys

if sys.version_info >= (3,):
    # The __module__ attribute is not writable in Python 3.
    # This test is not valid.
    pass
elif sys.platform == 'darwin':
    # This test fails on OS X, see
    # https://bugs.python.org/issue1170
    pass
else:
    print('__del__ called')
