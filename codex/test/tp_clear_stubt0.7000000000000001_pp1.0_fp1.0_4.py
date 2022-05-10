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

import unittest

class TestUnpickle(unittest.TestCase):
    def test_unpickle_lambda(self):
        # Test unpickling of lambdas
        self.assertEqual(pickle.loads(b"cos\nunpickle_lambda\nq\x00(csklearn.utils.fixes\nlinecacheq\x01Ntq\x02Rq\x03Rq\x04b.")(1), math.cos(1))

