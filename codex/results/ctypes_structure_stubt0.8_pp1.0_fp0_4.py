import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longdouble()
    foo = ctypes.CFUNCTYPE(S, ctypes.c_longdouble)

lib = ctypes.CDLL(find_library("m"))

lib.sin.argtypes = [ctypes.c_longdouble]
lib.sin.restype = ctypes.c_longdouble

lib.cos.argtypes = [ctypes.c_longdouble]
lib.cos.restype = ctypes.c_longdouble

lib.tan.argtypes = [ctypes.c_longdouble]
lib.tan.restype = ctypes.c_longdouble

lib.asin.argtypes = [ctypes.c_longdouble]
lib.asin.restype = ctypes.c_longdouble

lib.acos.argtypes = [ctypes.c_longdouble]
lib.acos.restype = ctypes.c_longdouble

lib.atan.argtypes = [ctypes.c_longdouble]
lib.atan.restype = ctypes.c_longdouble

lib.atan2.arg
