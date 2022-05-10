import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_int)
set_dmr_sim_error_distr_func = ctypes.CBTYPE( ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_int )
set_dmr_sim_error_distr_func .restype = ctypes.c_int
set_dmr_sim_error_distr_func .argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]

# Test ctypes.CFUNCTYPE(ctypes.c_int)
set_dmr_sim_error_distr_func = ctypes.CBTYPE( ctypes.c_int )
set_dmr_sim_error_distr_func .restype = ctypes.c_int
set_dmr_sim_error_distr_func .argtypes = []

# Test ctypes.CFUNCTYPE(ctypes.
