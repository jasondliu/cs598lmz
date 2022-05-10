import gc, weakref
import numpy as np
import pandas as pd
import pytest

from pandas.core.dtypes.common import is_list_like

import pandas.util.testing as tm
from pandas import (DataFrame, Series, Index, MultiIndex, Timestamp,
                    date_range, isna)
from pandas.core.indexes.datetimes import date_range
from pandas.core.indexes.period import period_range
from pandas.core.indexes.timedeltas import timedelta_range
from pandas.core.indexes.numeric import Int64Index
from pandas.core.indexes.range import RangeIndex
from pandas.core.indexes.multi import MultiIndex
from pandas.core.indexes.category import CategoricalIndex
from pandas.core.indexes.datetimelike import DatetimeIndex
from pandas.core.indexes.period import PeriodIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex
from pandas.core.indexes.interval import IntervalIndex
from
