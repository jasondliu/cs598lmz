import ctypes
# Test ctypes.CFUNCTYPE -- this must be the first ctypes_test otherwise
# the callbacks are still registered to the lib and crashes python
# when it exists, at least on Linux.

import unittest
