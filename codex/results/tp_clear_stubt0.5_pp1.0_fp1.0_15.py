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
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

class Test(unittest.TestCase):
    def test_memory_leak(self):
        self.assertIs(latefin.ref(), None)

if __name__ == "__main__":
    unittest.main()
