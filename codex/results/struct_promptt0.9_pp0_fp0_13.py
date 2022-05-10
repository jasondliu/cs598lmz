import _struct
# Test _struct.Struct

if _struct.Struct is None:
    import warnings
    warnings.warn("This test is skipped because _struct.Struct is not present")

import gc
import unittest
from test import test_support
from test.test_support import run_unittest


class StructTest(unittest.TestCase):
    
    def test_basics(self):
        # calculate required size
        alignment = _struct.calcsize('P')
        required_alignment = alignment - (_struct.Struct.size % alignment)
        required_size = _struct.Struct.size + required_alignment
        self.assertEqual(_struct.Struct.__basicsize__, required_size)

    def test_gc(self):
        # Issue #8329: PyStructObject is now tracked by the GC.
        weakrefs = weakref.ref(self)
        gc.collect()
        refs = gc.get_referents(weakrefs)
        self.assertEqual(len(refs), 2, repr(refs))     # for py3k:
