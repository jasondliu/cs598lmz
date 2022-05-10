import weakref

import numpy as np
import pandas as pd

from pandas.core.dtypes.common import (
    is_categorical_dtype,
    is_datetime64tz_dtype,
    is_extension_array_dtype,
    is_extension_type,
    is_list_like,
    is_object_dtype,
    is_re,
    is_scalar,
    is_string_like,
    needs_i8_conversion,
)
from pandas.core.dtypes.generic import (
    ABCDataFrame,
    ABCDatetimeIndex,
    ABCIndexClass,
    ABCSeries,
    ABCTimedeltaIndex,
)
from pandas.core.dtypes.missing import isna, notna

from pandas.core.arrays import ExtensionArray, ExtensionOpsMixin
from pandas.core.arrays.categorical import Categorical
from pandas.core.arrays.datetimes import DatetimeArrayMixin, DatetimeTZDtype
