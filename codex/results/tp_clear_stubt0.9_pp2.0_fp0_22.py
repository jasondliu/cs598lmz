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
del latefin

import gc
import unittest
from test import support


class GarbageCycle(unittest.TestCase):
    # Regression for http://bugs.python.org/issue5707.
    # A cycle that reaches back into its own __del__.
    def test_cycle(self):
        class C:
            def __init__(self):
                self.next = self
            def __del__(self):
                pass

        c = C()
        support.gc_collect()
        c.next = None
        support.gc_collect()


def test_main():
    support.run_unittest(GarbageCycle)


if __name__ == "__main__":
    test_main()
