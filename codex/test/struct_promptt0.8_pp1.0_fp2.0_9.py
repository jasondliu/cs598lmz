import _struct
# Test _struct.Struct when the format string uses standard size and alignment
# values.
import _testbuffer
import unittest
from test import support
from test.support import import_helper
TESTDIR = os.path.dirname(__file__) or os.curdir
FUZZ = 1e-6
os.environ[
    'PYTHON_TEST_NOPASS_HASHRANDOMIZATION'] = '1'
try:
    from collections.abc import MutableSequence
except ImportError:
    from collections import MutableSequence


def _big_float(x):
    x = float(x)
    if x == 0.0:
        x = 1e-100
    return x


class Fraction:

    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator


class _ArraySlicingTest:
    """Tests for slicing in the _array._array constructor."""

