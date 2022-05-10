import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# The following functions are declared in _ctypes_test.h:
#
# int func(int)
# int func_p(int *p)
# int func_pp(int **pp)
# int func_ppp(int ***ppp)
#

