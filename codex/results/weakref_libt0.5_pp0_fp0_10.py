import weakref

import numpy as np
import pytest

import pandas as pd
from pandas import DataFrame, Series, date_range, isna
import pandas._testing as tm
from pandas.core.arrays import ExtensionArray
from pandas.core.arrays.datetimes import DatetimeArray, DatetimeTZDtype
from pandas.core.arrays.period import PeriodArray, PeriodDtype
from pandas.core.dtypes.common import is_list_like
from pandas.core.dtypes.dtypes import CategoricalDtype
from pandas.core.dtypes.generic import ABCSeries

from .base import BaseExtensionTests


class BaseOpsTests:
    def test_is_monotonic(self):
        assert not self.all_data.is_monotonic_increasing
        assert not self.all_data.is_monotonic_decreasing
        assert not self.all_data.is_unique

    def test_shift(self):
        msg = "NotImplementedError: Series.shift is not implemented for type
