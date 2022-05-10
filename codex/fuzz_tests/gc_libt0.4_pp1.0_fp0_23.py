import gc, weakref
import numpy as np
import pandas as pd
import pytest

from datetime import datetime, date, time
from pandas import (Series, DataFrame, Panel, MultiIndex,
                    Timestamp, DatetimeIndex, TimedeltaIndex,
                    date_range, timedelta_range,
                    Index, Int64Index, Float64Index,
                    UInt64Index, Categorical, CategoricalIndex,
                    PeriodIndex, RangeIndex, IntervalIndex,
                    Int64Index, MultiIndex, IntervalIndex)
from pandas.compat import long, lrange, lmap, range, zip
from pandas.util import testing as tm

import pandas.util.testing as tm

from pandas.core.index import (Index, _ensure_index, _get_na_value,
                               _get_na_value_box, _ensure_frozen,
                               _ensure_has_len, _ensure_int64,
                               _ensure_platform_int, _ensure_object,
                               _ensure_int_or
