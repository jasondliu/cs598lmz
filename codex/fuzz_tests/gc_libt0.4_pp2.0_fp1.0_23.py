import gc, weakref
import numpy as np
import pandas as pd
import pytest

from pandas import (
    DataFrame,
    Index,
    MultiIndex,
    Series,
    date_range,
    period_range,
    timedelta_range,
)
import pandas._testing as tm
from pandas.core.arrays import ExtensionArray
from pandas.core.arrays.datetimes import DatetimeArray, TimedeltaArray
from pandas.core.arrays.period import PeriodArray
from pandas.core.arrays.sparse import SparseArray
from pandas.core.dtypes.common import is_categorical_dtype, is_datetime64_any_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype
from pandas.core.dtypes.generic import ABCIndexClass, ABCSeries
from pandas.core.dtypes.missing import isna
from pandas.util import testing as assert_util

from pandas.tests.extension.base import BaseOpsUtil


class BaseArithmeticOps:
   
