import gc, weakref

try:
    import cPickle as pickle
except ImportError:
    import pickle

from numpy.testing import *

from numpy.compat import asbytes, asunicode

class TestPickle(TestCase):
    def test_pickle(self):
        a = arange(10)
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            s = pickle.dumps(a, proto)
            b = pickle.loads(s)
            assert_array_equal(a, b)

    def test_pickle_0d(self):
        a = array(3)
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            s = pickle.dumps(a, proto)
            b = pickle.loads(s)
            assert_array_equal(a, b)

    def test_pickle_dtype(self):
        dt = dtype([('f1', int), ('f2', float), ('f3', complex)])
       
