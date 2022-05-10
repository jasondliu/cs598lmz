import weakref

import numpy as np
import pytest

import pandas as pd
import pandas._testing as tm
from pandas.core.arrays import Categorical, CategoricalDtype, DatetimeArray
from pandas.core.dtypes.common import is_categorical_dtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries

import pandas.core.algorithms as algos
import pandas.core.common as com

from pandas import CategoricalIndex, DataFrame, Index, Series, Timestamp, date_range
import pandas.util.testing as tm
from pandas.util.testing import assert_almost_equal


class TestMatch:
    def test_ints(self):
        values = [0, 2, 1]
        to_match = [0, 1, 2, 2, 0, 1, 3, 0]

        result = algos.match(to_match, values)
