import weakref
import platform
import os
import collections
import re

if sys.version_info >= (3,):
    xrange = range
    basestring = unicode = str
    long = int
    from io import StringIO
    from functools import reduce

_PY2 = sys.version_info[0] == 2
_PY3 = sys.version_info[0] == 3

if _PY3:
    from . import _cffi_backend
else:
    from . import _ctypes_backend

if sys.version_info >= (2,7):
    from collections import OrderedDict
else:
    from ordereddict import OrderedDict

#
# NOTE: This file is included in both Python 2 and Python 3 environments,
#       so you need to be very careful about what you import.
#


#
# Some helper functions.
#

def _iteritems(d):
    """
    Iterate over items of (potentially) non-Python-2-compatible dictionary.
    """
