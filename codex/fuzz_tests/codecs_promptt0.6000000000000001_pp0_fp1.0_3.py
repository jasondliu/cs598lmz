import codecs
# Test codecs.register_error('strict', codecs.strict_errors)

import pytest
from six import PY3

from numpy import array, dtype, int32, float32, nan
from numpy.testing import assert_equal

from pandas import DataFrame, Series, isnull, notnull, bdate_range
from pandas.tseries.index import date_range
from pandas.tseries.offsets import BDay
import pandas.tseries.offsets as offsets
from pandas.compat import lrange, range, zip, u, StringIO
from pandas.io.date_converters import parse_time_string
from pandas.util.testing import (assert_series_equal,
                                 assert_frame_equal,
                                 assert_almost_equal)
import pandas.util.testing as tm
import pandas as pd

from pandas.io.common import _sanitize_dates
from pandas.io.parsers import read_csv
from pandas.io.stata import read_stata
from pandas.io.stata import write
