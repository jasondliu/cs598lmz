import weakref
import warnings
from numbers import Integral
from copy import copy
from time import time

import numpy as np
from numpy import ma
from numpy.ma.mrecords import MaskedRecords

from . import MaskedConstantError
from .maskedarray import _check_fill_value, _extras_test_methods
from ._sharedmask import (sharedmask, _sharedmask,
                          _maybe_view_as_subclass, _getdata)
from .extras import (set_fill_value, get_fill_value, masked_all, masked_print_option,
                     unmasked_contiguous, masked, is_masked, masked_array,
                     mask_or, getmaskarray, getmask, is_mask, mask_rowcols,
                     masked_values, masked_invalid, hardmask_invalid, softmask_invalid,
                     masked_equal)
from .util import (fastCopyAndTranspose, _validate_axis, isSequenceType)

#----------------------------------------------------------------------
class _MaskedConstant (object):
    """Base class for
