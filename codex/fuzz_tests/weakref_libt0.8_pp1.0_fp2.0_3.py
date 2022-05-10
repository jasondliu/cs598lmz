import weakref
import re
import math
#
from ._gp_dtype import get_dtype_from_typename
from ._c_api_extension import (
    PyIntSlice,
    PySlice_Unpack,
    PyLSlice_Unpack,
    PyRange_Unpack,
    PyNoSupportElemCall,
    PyNoSupportShapeCall,
    get_python_numeric_round,
)
#
from .gftools import GfTools

#---------------------------------------------------------------------------
# Utility functions for Python
#
def _is_int(obj):
    return isinstance(obj, int)

def _is_float(obj):
    return isinstance(obj, float)

def _is_str(obj):
    return isinstance(obj, str)

#---------------------------------------------------------------------------
# Abstract Base Class for 1D objects
#
class _Gf1DBase(metaclass=abc.ABCMeta):
    """Abstract Base Class (ABC) for all 1D objects.

    All Gf1DBase objects expose three C-level methods:
        * `_
