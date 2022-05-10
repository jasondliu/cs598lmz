import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
#
# Check that a given collection removes collectable objects from
# from the collectable list.  Also check that collectable
# produces the expected results for normal, non-collectable
# objects.
#
# XXX Too many tests, should be broken up into separate tests

import gc
from test.test_support import run_unittest

from weakref import proxy, ref
import sys
from collections import Iterable
from functools import reduce
from types import BuiltinMethodType, InstanceType, MethodType, FunctionType
from int import Int
from weakref_test import none

# Be careful with the assertTrue() calls in this module:
# Sometimes the code under test issues a warning, and the
# warnings module changes sys.stdout.  We must save and restore
# sys.stdout to avoid failing, e.g.,
# AssertionError: True is not false : <open file '<stdout>', mode 'w' at 0x00A719D0>
#     != <open file '<stderr>', mode 'w' at 0x00A71A
