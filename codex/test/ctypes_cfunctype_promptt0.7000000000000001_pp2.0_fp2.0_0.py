import ctypes
# Test ctypes.CFUNCTYPE.  This must be done separately from test_ctypes, since
# on some platforms (OS X 10.6 or 10.7) ctypes will segfault when imported at
# module level.
import unittest
