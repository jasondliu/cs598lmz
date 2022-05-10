import ctypes
# Test ctypes.CFUNCTYPE(T).from_address(T)
#
# This test is to check that from_address() works for
# all callable ctypes types (ctypes function, ctypes instance method,
# ctypes class method, ctypes static method).

import unittest
