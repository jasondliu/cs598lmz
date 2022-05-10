import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.
#
# 1. Do not collect non-collectable garbage.
#
# 2. Raise an error when a weakref is created to a type.
#
# 3. Collect still-alive weakrefs for non-collectable garbage.
#
# 4. Raise an error when a weakref is created to a type.
#
# 5. Collect dead weakrefs for non-collectable garbage.
#
# 6. Do not collect still-alive weakrefs for collectable garbage.
#
# 7. Collect dead weakrefs for collectable garbage.

import sys
import unittest
import weakref
import gc

from test import support
from test import mapping_tests
import types
from io import IOBase


def R():
    pass
RRef = weakref.ref(R)
class G:
    pass
class X:
    pass
class Y:
    pass

class WeakRefTest(unittest.TestCase):

    #
    # 1. Do not collect non-collectable garbage.
    #
    def test_gc
