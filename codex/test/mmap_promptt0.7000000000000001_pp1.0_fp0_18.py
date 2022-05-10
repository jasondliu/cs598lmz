import mmap
# Test mmap.mmap(0, 1, "MapView")
assert_raises(TypeError, mmap.mmap, 0, 1, "MapView")

import os
import sys
import mmap
import _testcapi

# Verify that we get the expected errors on mmap(0, 1, "MapView")
if sys.platform == "win32":
    # On Windows, mmap(0, 1, "MapView") raises WindowsError.
    assert_raises(WindowsError, mmap.mmap, 0, 1, "MapView")
else:
    # On UNIX, mmap(0, 1, "MapView") raises TypeError.
    assert_raises(TypeError, mmap.mmap, 0, 1, "MapView")

