import weakref

import numpy as np
import pytest

import pandas as pd
from pandas import Index, MultiIndex, Series, date_range, isna
import pandas._testing as tm


class TestSeries:
    def test_series_constructor(self, datetime_series):
        # assert Series are constructed
        assert datetime_series.dtype == np.dtype("M8[ns]")

        assert isinstance(datetime_series.index, Index)
        assert isinstance(datetime_series, Series)

    def test_constructor_name(self, datetime_series):
        # GH 1802
        s = Series(datetime_series, name="foo")
        assert s.name == "foo"

    def test_constructor_name_index(self, datetime_series):
        # GH 1802
        s = Series(datetime_series, name="foo", index=datetime_series.index)
        assert s.name == "foo"

    def test_constructor_series_name(self, datetime_series):
        #
