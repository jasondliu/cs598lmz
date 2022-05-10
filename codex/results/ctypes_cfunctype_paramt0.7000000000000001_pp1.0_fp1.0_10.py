import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER( ctypes.c_float))
#FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER( ctypes.c_float), ctypes.c_int)

class _Gx(object):
    _lib_path = os.path.join(os.path.dirname(__file__), 'libgx.so')
    _lib = ctypes.cdll.LoadLibrary(_lib_path)
    _lib.gx_create.restype = ctypes.c_void_p
    _lib.gx_destroy.argtypes = [ctypes.c_void_p]
    _lib.gx_set_sample_rate.argtypes = [ctypes.c_void_p, ctypes.c_double]
    _lib.gx_set_tempo
