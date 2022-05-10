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

for i in range(1000):
    try:
        latefin.__del__()
    except TypeError:
        break
    else:
        print(i)

import unittest

class TestWeakrefType(unittest.TestCase):
    def test_weakref_to_type(self):
        t = type(self)
        r = weakref.ref(t)
        self.assertEqual(r(), t)

    def test_weakref_to_type_subclass(self):
        t = type(self)
        class T(type(self)):
            pass
        r = weakref.ref(T)
        self.assertEqual(r(), T)

    def test_weakref_to_newstyle_class(self):
        t = type(self)
        class T(object):
            pass
        r = weakref.ref(T)
        self.assertEqual(r(), T)

    def test_weakref_to_oldstyle_class(self):
        t = type(
