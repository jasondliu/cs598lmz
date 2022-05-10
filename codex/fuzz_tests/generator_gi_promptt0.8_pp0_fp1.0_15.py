gi = (i for i in ())
# Test gi.gi_code.co_flags
next(gi)

# Test abstractmethod
from abc import ABCMeta
class C(metaclass=ABCMeta):
    @abc.abstractmethod
    def foo(self):
        pass

# Test issubclass
class D:
    pass
class E(D):
    pass
issubclass(E, D)

# Test pickling of iterators
import pickle, io
from test import support

def pickle_iterator(it):
    return pickle.loads(pickle.dumps(it))

def test_pickle(it, expected):
    it = pickle_iterator(it)
    support.unlink(support.TESTFN)
    with open(support.TESTFN, "wb") as f:
        pickle.dump(it, f)
    with open(support.TESTFN, "rb") as f:
        it = pickle.load(f)
    it = pickle_iterator(it)
    result = list(it)
    assert result == expected

def test_pickling_iter
