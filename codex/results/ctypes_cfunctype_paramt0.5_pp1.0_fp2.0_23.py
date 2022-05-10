import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class PyEvent(ctypes.Structure):
    _fields_ = [('ev_base', ctypes.c_void_p),
                ('ev_callback', FUNTYPE),
                ('ev_arg', ctypes.c_void_p),
                ('ev_fd', ctypes.c_int),
                ('ev_events', ctypes.c_short),
                ('ev_res', ctypes.c_short),
                ('ev_flags', ctypes.c_int),
                ('ev_ncalls', ctypes.c_int),
                ('ev_pncalls', ctypes.c_void_p)]

class PyEventBuffer(ctypes.Structure):
    _fields_ = [('buf', ctypes.c_void_p),
                ('orig_buf', ctypes.c_void_p),
                ('misalign', ctypes.c_int),
                ('size', ctypes.c_int),
                ('max_size', ctypes.c_int),
                ('off', ctypes.c_int),
                ('len', c
