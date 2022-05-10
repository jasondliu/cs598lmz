import ctypes
ctypes.cast(0, ctypes.py_object)

import sys
import os
import inspect
import ctypes
import _ctypes

# This module provides ctypes with the ability to call functions
# exported from dlls/shared libraries.  It does not (yet) provide
# the ability to access variables exported from dlls/shared
# libraries.  The exported functions can be called as if they were
# Python functions.

# Notes:
#
# [1] "dll" is used here to mean "dynamically loadable library".  It is
# used in a non-platform specific way.  For example, dlopen() is used
# on unix, and LoadLibrary() is used on Windows.
#
# [2] "cdll" is used here to mean "CDLL", a subclass of "dll".
#
# [3] "handle" is used here to mean a dll handle as returned by
# dlopen() or LoadLibrary().  This is different from a "handle" as
# defined by Windows.  On Windows, a "handle" is an opaque pointer.
#
# [4
