import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# XXX This is a hack:
# The _ctypes_test module does not have a function
# named _testfunc_p_p anymore, but ctypes should
# still be able to call it.  This hack makes the
# old name point to the new name.
lib._testfunc_p_p = lib._testfunc_p_p_p

# XXX This is a hack, too:
# The _ctypes_test module does not have a function
# named _testfunc_p_p_p anymore, but ctypes should
# still be able to call it.  This hack makes the
# old name point to the new name.
lib._testfunc_p_p_p = lib._testfunc_p_p_p_p

# XXX This is a hack, too:
# The _ctypes_test module does not have a function
# named _testfunc_p_p_p_p anymore, but ctypes should
# still be able to call it.
