import gc, weakref, threading
import sys, os, copy
import traceback, warnings
from six import integer_types, iteritems, string_types

from . import _tools, _types, _structures
from . import _dtypes
from . import _deserialize
from . import _serialize
from . import _finders
from . import _errors
from . import _internals
from . import _drv
from . import _api_types
from . import _algorithm
from . import _ops
from . import _property
from . import _internal_utils
from . import _base


##----------------------------------------------------------------------------------------------------------------------
## Class attr methods
##----------------------------------------------------------------------------------------------------------------------

def _get_classname(instance):
    return instance.__class__.__name__


##----------------------------------------------------------------------------------------------------------------------
## Array Attr methods
##----------------------------------------------------------------------------------------------------------------------

def _isarray(instance):
    """
    This method checks whether the array is a thin or thick array(numpy.ndarray, cupy.ndarray, or cudf.Series)
    """
    classname = _get_classname(
