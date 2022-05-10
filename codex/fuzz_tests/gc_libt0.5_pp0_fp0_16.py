import gc, weakref

from . import _flt_info
from ._flt_info import (
    FLT_RADIX, FLT_ROUNDS, FLT_MANT_DIG,
    FLT_MIN_EXP, FLT_MAX_EXP, FLT_MIN, FLT_MAX,
    DBL_MANT_DIG, DBL_MIN_EXP, DBL_MAX_EXP, DBL_MIN, DBL_MAX
)
from ._flt_info import (
    LDBL_MANT_DIG, LDBL_MIN_EXP, LDBL_MAX_EXP, LDBL_MIN, LDBL_MAX
)
from ._flt_info import (
    DIG, MANT_DIG, MIN_EXP, MAX_EXP, MIN, MAX,
    FLT_DIG, DBL_DIG, LDBL_DIG
)
from ._flt_info import (
    FLT_EPSILON, DBL_EPSILON, LDBL_EPSILON,
    FLT_MIN_10_EXP, FLT_MAX_
