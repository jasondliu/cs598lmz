import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a little more complicated than the other tests, because we
# want to test the functionality of ctypes.CFUNCTYPE itself, not just
# the functionality of the CFUNCTYPE instances.
#
# Therefore, we test that the CFUNCTYPE factory function returns the
# appropriate types for different kinds of functions, and then we test
# that the created types have the appropriate signatures.
#
# We don't test the actual calling of the functions, just the
# signatures.
import sys
import unittest
