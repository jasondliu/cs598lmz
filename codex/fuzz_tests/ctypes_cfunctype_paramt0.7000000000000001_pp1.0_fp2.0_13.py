import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

if not hasattr(ctypes,"c_ssize_t"):
    ctypes.c_ssize_t = ctypes.c_long

class PyCapsule(ctypes.Structure):
    _fields_ = [
        ("pointer", ctypes.c_void_p),
        ("name", ctypes.c_char_p),
        ("context", ctypes.c_void_p),
        ("destructor", ctypes.c_void_p),
    ]

class PyThreadState(ctypes.Structure):
    _fields_ = [
        ("next", ctypes.POINTER(PyThreadState)),
        ("interp", ctypes.c_void_p),
        ("frame", ctypes.c_void_p),
        ("recursion_depth", ctypes.c_int),
        ("tstate_flags", ctypes.c_int),
        ("sys_profile_func", ctypes.c_void_p),
        ("sys_trace_func", ctypes.c_void_p),
        ("curexc
