import ctypes
# Test ctypes.CFUNCTYPE

# This test is specific to the i386 architecture.

import sys

if sys.platform != "win32":
    raise ImportError("test_cfnctype is specific to Windows")

from ctypes import *

# Check the size of an integer.

if sizeof(c_int) != 4:
    raise ImportError("test_cfnctype is specific to 32-bit Windows")

# Check the size of a pointer.

if sizeof(c_void_p) != 4:
    raise ImportError("test_cfnctype is specific to 32-bit Windows")

# Check the size of a long long.

if sizeof(c_longlong) != 8:
    raise ImportError("test_cfnctype is specific to 32-bit Windows")

# Check the size of a long double.

if sizeof(c_longdouble) not in (12, 16):
    raise ImportError("test_cfnctype is specific to 32-bit Windows")

# Check the size of wchar_t.

if sizeof(c_wchar) != 2:
