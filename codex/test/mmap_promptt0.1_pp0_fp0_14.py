import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED)

import os
import sys
import time
import traceback
import types
import unittest

import _testcapi

# Test the Py_ssize_t typedef
import sys
if sys.maxsize > 2**32:
    assert _testcapi.sizeof_Py_ssize_t == 8
else:
    assert _testcapi.sizeof_Py_ssize_t == 4

# Test the Py_ssize_t typedef
import sys
if sys.maxsize > 2**32:
    assert _testcapi.sizeof_Py_ssize_t == 8
else:
    assert _testcapi.sizeof_Py_ssize_t == 4

# Test the Py_UNICODE typedef
assert _testcapi.sizeof_Py_UNICODE == 2

# Test the Py_UCS4 typedef
assert _testcapi.sizeof_Py_UCS4 == 4

# Test the Py_hash_t typedef
assert _
