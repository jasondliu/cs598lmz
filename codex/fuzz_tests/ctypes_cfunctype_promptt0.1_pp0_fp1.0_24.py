import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function pointer
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lib._testfunc_p_p)

# a function pointer to a function pointer
fp = ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))
fp.from_address(lib._testfunc_p_p).contents

# a function pointer to a function pointer to a function pointer
fpp = ctypes.POINTER(fp)
fpp.from_address(lib._testfunc_p_p).contents.contents

# a function pointer to a function pointer to a function pointer to a function pointer
fppp = ctypes.POINTER(fpp)
fppp.from_address(lib._testfunc_p_p).contents.contents.contents

# a function pointer to a function pointer to a function pointer to a function pointer to a function
