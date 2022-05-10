import mmap
# Test mmap.mmap(-1, size, prot=mmap.PROT_EXEC, flags=mmap.MAP_PRIVATE)

# This tests the case where the size is not a valid page size.
# On Windows, this should fail.

import mmap
import unittest
from test import support

@unittest.skipUnless(hasattr(mmap, 'PROT_EXEC'),
                     'mmap.PROT_EXEC required for this test.')
class MmapExecTests(unittest.TestCase):
    def test_exec_size(self):
        size = mmap.PAGESIZE + 1
        self.assertRaises(ValueError, mmap.mmap, -1, size, prot=mmap.PROT_EXEC,
                          flags=mmap.MAP_PRIVATE)

def test_main():
    support.run_unittest(MmapExecTests)

if __name__ == "__main__":
    test_main()
