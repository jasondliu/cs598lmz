import gc, weakref

import numpy as np
import pandas as pd
import pytest

from pandas import DataFrame, Series, Timestamp, date_range, isna
import pandas._testing as tm
from pandas.core.arrays import ExtensionArray
from pandas.core.dtypes.common import is_list_like
from pandas.core.dtypes.dtypes import CategoricalDtype
from pandas.core.dtypes.generic import ABCSeries, ABCIndexClass
from pandas.core.dtypes.missing import isna, notna

from pandas.core.arrays.categorical import (
    Categorical,
    CategoricalAccessor,
    CategoricalDtype,
    _factorize_from_iterable,
    _get_codes_for_values,
    _get_codes_for_values_map,
    _get_codes_for_values_set,
    _get_codes_for_values_na_map,
    _get_codes_for_values_na_set,
    _get_codes_for_values
