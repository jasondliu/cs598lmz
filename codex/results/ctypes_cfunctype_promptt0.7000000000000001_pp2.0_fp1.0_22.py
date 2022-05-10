import ctypes
# Test ctypes.CFUNCTYPE()
import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

func = ctypes.CFUNCTYPE(ctypes.c_int)(("testfunc_cb", lib))

print func(1, 2)


# Test callback functions
func.restype = ctypes.c_int
func.argtypes = (ctypes.c_int, ctypes.c_int)

print func(1, 2)

# Test the array members of callback functions
func.restype = None
func.argtypes = (ctypes.c_int * 2, )
func(range(2))

func.restype = None
func.argtypes = (POINTER(ctypes.c_int * 2), )
func((ctypes.c_int * 2)(*range(2)))

func.restype = None
func.argtypes = (POINTER(ctypes.c_int * 2), )
func((ctypes.c_int * 2)(1, 2))

func.restype = None
func.argtypes = (ct
