import _struct
from numpy import int8, int16, int32, int64
from numpy import uint8, uint16, uint32, uint64
from numpy import float32, float64, float16
from numpy import datetime64, timedelta64

from .core import (
    Categorical,
    CategoricalDtype,
    Period,
    PeriodDtype,
)


def is_object_dtype(arr_or_dtype):
    return lib.is_object_dtype(arr_or_dtype)


def is_datetime64_dtype(arr_or_dtype):
    return lib.is_datetime64_dtype(arr_or_dtype)


def is_datetime64tz_dtype(arr_or_dtype):
    return lib.is_datetime64tz_dtype(arr_or_dtype)


def is_timedelta64_dtype(arr_or_dtype):
    return lib.is_timedelta64_dtype(arr_or_dtype)


