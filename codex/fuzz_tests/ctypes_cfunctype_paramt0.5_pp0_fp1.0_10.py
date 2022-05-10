import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class PyThreadState(ctypes.Structure):
    _fields_ = [("next", ctypes.c_void_p),
                ("interp", ctypes.c_void_p),
                ("frame", ctypes.c_void_p),
                ("recursion_depth", ctypes.c_int),
                ("tracing", ctypes.c_int),
                ("use_tracing", ctypes.c_int),
                ("c_profilefunc", FUNTYPE),
                ("c_tracefunc", FUNTYPE),
                ("curexc_type", ctypes.c_void_p),
                ("curexc_value", ctypes.c_void_p),
                ("curexc_traceback", ctypes.c_void_p),
                ("exc_type", ctypes.c_void_p),
                ("exc_value", ctypes.c_void_p),
                ("exc_traceback", ctypes.c_void_p),
                ("dict", ctypes.c_void_p),
                ("tick_counter", ctypes
