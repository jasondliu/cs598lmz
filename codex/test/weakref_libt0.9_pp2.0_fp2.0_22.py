import weakref
import unittest
from numpy.testing import assert_equal
from numpy.testing.decorators import skipif

from numpy.testing.utils import skipif_nonmatlab
from scipy import signal
from scipy.signal import sigtools


def _assert_valid(x, pad=False):
    try:
        assert (x.flags.f_contiguous or x.flags.c_contiguous)
    except AttributeError:
        if not pad:
            raise


def _assert_valid_1d(x, pad=False):
    _assert_valid(x, pad)
    assert x.ndim == 1


class TestSigTools(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_mode_arguments(self):
        # valid_modes should include an entry for each allowed modename
        valid_modes = dict((v, k) for k, v in
                           [(1, 'same'), (0, 'valid'), (-1, 'full')])

