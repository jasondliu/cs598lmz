import ctypes
# Test ctypes.CFUNCTYPE(), ctypes.FUNCFLAG_USE_ERRNO, ctypes.Py_ssize_t.
#
# This test is run by buildbot, do not add any dependencies which have
# not been released yet.

from ctypes import *
import unittest
