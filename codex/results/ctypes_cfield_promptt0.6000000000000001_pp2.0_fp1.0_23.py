import ctypes
# Test ctypes.CField from bug #37753.  It was crashing at the time.
import _ctypes
_ctypes.CField = ctypes.CField

import _testcapi

import unittest
from test import support
from test.support import bigmemtest, bigaddrspacetest

have_unicode = support.have_unicode

# A list of all types that have a "size" attribute.
#
# This list is a list of tuples (type, minimum_size).  If a type has the
# "size" attribute, then the minimum size is checked and must be greater
# than or equal to the value given in the list.  This is used to specify
# the minimum size of the type (or of instances of the type).
#
# Note that the size is given in bytes.  This is for consistency with the
# sizeof function.
types_with_size = [
    (type(None), 0),
    (type(Ellipsis), 0),
    (bool, 1),
    (int, 1),
    (float, 8),
    (complex, 16),
    (slice
