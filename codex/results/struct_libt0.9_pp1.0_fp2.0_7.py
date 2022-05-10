import _struct
from numpy import add, array, arange, empty, full, frombuffer, uint32
from numpy.random import randint
from pytest import raises as assert_raises
from uuid import UUID

from pandas import DataFrame, UInt32Dtype
from pandas._libs.tslibs.timezones import all_timezones, dateutil_gettz
from pandas.core.arrays import IntegerArray, PandasDtype

from pandas.core.arrays.integer import _INT64_DTYPE
from pandas.core.dtypes.common import is_dtype_equal
from pandas.core.dtypes.generic import ABCIndexClass, ABCIndex, ABCSeries
from pandas.core.dtypes.missing import isna


class TestPandasDtypeFormatting:
    def test_str(self):
        dt = UInt32Dtype()
        assert str(dt) == "uint32"

    def test_repr(self):
        dt = UInt32Dtype()
        assert repr(dt) == "UInt32D
