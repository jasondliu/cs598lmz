import ctypes
# Test ctypes.CFUNCTYPE()
# This tests that the C compiler supports the C99 'restrict' keyword.
def test_cfunctype():
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_float)

try:
    test_cfunctype()
except:
    raise DistutilsPlatformError, \
          "Cannot compile with the C99 'restrict' keyword"

#
# Check for ctypes
#

try:
    import ctypes
except ImportError:
    raise DistutilsPlatformError, "Cannot compile with 'ctypes' module installed"

#
# Check for long double support
#

if not _check_long_double():
    raise DistutilsPlatformError, "Cannot compile with 'long double' support"

#
# Check for IEEE 754 compliance
#

if not _check_ieee_754():
    raise DistutilsPlatformError, "Cannot compile with IEEE 754 compliance"

#
# Check for C99 support
# Note that this is
