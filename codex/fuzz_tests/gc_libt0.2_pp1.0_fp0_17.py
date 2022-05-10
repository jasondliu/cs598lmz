import gc, weakref
import numpy as np
import pandas as pd
import pytest

from pandas.compat import PY3

from pandas.core.dtypes.common import is_list_like

import pandas.util.testing as tm
from pandas.util.testing import assert_series_equal
from pandas.tests.frame.common import TestData


class TestSeries(TestData):

    def test_rename(self):
        series = Series(np.random.randn(3), index=['a', 'b', 'c'], name='x')

        renamed = series.rename('y')
        assert renamed.name == 'y'

        renamed = series.rename(name='y')
        assert renamed.name == 'y'

        # dict
        renamed = series.rename({'x': 'y'})
        assert renamed.name == 'y'

        # partial dict
        renamed = series.rename({'x': 'y', 'a': 'b'})
        assert renamed.name == 'y'

        # function
        renamed =
