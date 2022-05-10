import weakref

import numpy as np
import pytest

from pandas import (
    DataFrame,
    Index,
    MultiIndex,
    Series,
    date_range,
    isna,
    notna,
    period_range,
    timedelta_range,
)
import pandas._testing as tm
from pandas.core.arrays import Categorical
from pandas.core.arrays.sparse import SparseArray
from pandas.core.arrays.sparse.tests.test_sparse import _test_data
from pandas.core.indexes.datetimes import DatetimeIndex
from pandas.core.indexes.period import PeriodIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex
from pandas.core.sparse.api import SparseDtype
from pandas.core.sparse.scipy_sparse import SparseSeries
from pandas.core.sparse.tests.test_sparse_array import SparseSeriesCheck


