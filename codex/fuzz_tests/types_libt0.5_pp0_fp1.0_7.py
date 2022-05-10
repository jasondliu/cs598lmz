import types
types.FunctionType = type(lambda x: x)

import numpy as np
import pytest

import pandas as pd
from pandas import DataFrame, Series, Timestamp, date_range, isna
import pandas._testing as tm
from pandas.core.arrays.datetimes import DatetimeArray, TimedeltaArray
from pandas.core.arrays.timedeltas import _TimedeltaLikeArrayMixin
from pandas.core.arrays.timestamps import _TimestampLikeArrayMixin
from pandas.core.dtypes.dtypes import DatetimeTZDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCIndexClass, ABCSeries
from pandas.core.dtypes.missing import isna
from pandas.core.indexes.datetimes import TimedeltaIndex
from pandas.core.indexes.period import PeriodIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex
from pandas.core.indexes.timestamps import Timestamp
from pandas.core.series import Series


