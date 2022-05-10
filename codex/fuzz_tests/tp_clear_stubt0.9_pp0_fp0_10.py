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
del func, cyc, LateFin, Cyclic
gc.collect()

 
latefin = LateFin()
del LateFin
gc.collect()

weakref.WeakKeyDictionary({ latefin: None })
#$
'''


import unittest
import sys
from support import captured_io

class TestUnreachableSymbols(unittest.TestCase):

    def test_unreachable_symbol(self):
        with captured_io(1) as (out, err):
            self.assertRaises(ImportError, __import__,
                              "unreachable_symbol")
        self.assertRaises(AttributeError, eval, "unreachable_symbol",
                          {}, {})

    def test_undefined_symbols(self):
        from test.test_gc import UndefinedSymbols, Dummy
        class Dummy2(Dummy): pass
        for cls in Dummy, Dummy2, UndefinedSymbols:
            self.assertEqual(hasattr(cls, "has"), False)
            self.assertEqual(
