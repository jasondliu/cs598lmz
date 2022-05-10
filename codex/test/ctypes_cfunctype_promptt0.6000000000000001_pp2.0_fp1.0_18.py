import ctypes
# Test ctypes.CFUNCTYPE

# This test is needed to make sure that the return value of
# ctypes.CFUNCTYPE(resulttype, *paramtypes) is a callable object, which
# is neither a class nor a type object.  (It is a wrapper object,
# which is callable.)

import unittest
