import gc, weakref
import sys

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

import unittest

from sklearn.datasets.samples_generator import make_classification
from sklearn import svm
from sklearn.utils.testing import assert_less
from sklearn.utils.testing import assert_greater_equal
from sklearn.utils.testing import assert_greater
from sklearn.utils.testing import assert_less_equal
from sklearn.utils.testing import assert_raises
from sklearn.utils.testing import assert_raises_regexp
from sklearn.utils.testing import assert_true
from sklearn.utils.testing import assert_false
from sklearn.utils.testing import assert_equal
from sklearn.utils.testing import assert_array_almost_equal
from sklearn.utils.testing import assert_array_equal
from sklearn.utils.testing import assert_array_less
from sklearn.utils.testing import assert_equal
from sklearn.utils.testing import assert_not_equal
from sklearn.utils
