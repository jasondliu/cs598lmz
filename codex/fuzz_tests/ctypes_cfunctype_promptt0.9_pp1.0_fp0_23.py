import ctypes
# Test ctypes.CFUNCTYPE by wrapping drand48
rand_t = ctypes.CFUNCTYPE(ctypes.c_double)
lib = ctypes.CDLL(None)
drand48 = lib.drand48
assert drand48() != 0, 'drand48() returned 0' # sanity check
rand48 = rand_t(drand48)
assert rand48() != 0, 'drand48 returned 0'   # sanity check
# Test that PyCFuncPtrType is callable
assert isinstance(drand48, ctypes.PyCFuncPtrType)
drand48() != 0, 'drand48 returned 0'         # sanity check
drand49 = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.c_int,
                           ctypes.c_int, ctypes.POINTER(ctypes.c_int))(
        lib.drand48)
assert drand49(0, 0, 0, None) != 0, 'drand48 returned 0' # sanity check
drand50 = ctypes.CFUNCTYPE(
