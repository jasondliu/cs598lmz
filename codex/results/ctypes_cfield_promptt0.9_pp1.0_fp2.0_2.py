import ctypes
# Test ctypes.CField
from ctypes.test.test_cfield import *

# XXX test for memory leaks
from ctypes.test.test_backend import _test_backend
_test_backend(ctypes)

from ctypes.test.test_malloc_free import _test_malloc_free
_test_malloc_free(ctypes.cast)

from ctypes.test.test_errcheck import _test_errcheck
_test_errcheck(ctypes)

from ctypes.test.test_inspect import _test_inspect_getmembers, _test_inspect
_test_inspect_getmembers(ctypes)
_test_inspect(ctypes)

# FIXME: test for ctypes helpers:
# test for Stucture
from ctypes.test.test_structure import *
from ctypes.test.test_unions import *
from ctypes.test.test_stdcall import *
from ctypes.test.test_nested_structures import *
from ctypes.test.test_alignment import *
from ctypes.test.
