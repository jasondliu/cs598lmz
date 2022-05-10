import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,
       ctypes.POINTER(barsoi_float_t),
       ctypes.c_int,
       ctypes.POINTER(barsoi_arma_mat),
       ctypes.c_int,
       ctypes.POINTER(barsoi_arma_vec),
       ctypes.POINTER(ctypes.c_void_p),
       ctypes.POINTER(ctypes.c_void_p),
       ctypes.c_int,
       ctypes.c_void_p)

class barsoi_options_t(ctypes.Structure):
    _fields_ = [
            ("max_iter",       ctypes.c_uint32),
            ("max_iter_no_dec",ctypes.c_uint32),
            ("tolerance",      ctypes.c_float),
            ("mu_main",        ctypes.c_float),
            ("mu_correction",  ctypes.c_float),
            ("mu_termination", ctypes.c_float),
            ("initial_X",      ctypes.c_int),
