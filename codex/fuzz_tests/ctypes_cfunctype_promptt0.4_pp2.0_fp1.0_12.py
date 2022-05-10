import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a bit more complex than the others, because it
# tests a feature that is not directly related to Python, but
# to the C compiler and the C library.
#
# The test checks that ctypes can call functions that take
# variable arguments, such as printf.  This is implemented
# by using the cdecl calling convention.  The cdecl calling
# convention is the default on Windows and most Unix platforms,
# but some Unix platforms such as HP-UX use the stdcall convention
# as the default.  To test this, we must find out which calling
# convention the C compiler uses, and then call a function
# with the other calling convention.  We use the fact that
# printf is a variadic function, and that the va_* macros
# are defined in stdarg.h, to find out which calling convention
# printf uses.

# XXX We should also test that we can call functions with the
# XXX stdcall calling convention on Windows.

import sys
import os
import unittest
from ctypes import *
from ctypes.test import need_symbol

class CFuncPtr
