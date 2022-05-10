import ctypes

class S(ctypes.Structure):
    x = None

S._fields_ = [('x',
               ctypes.POINTER(ctypes.c_void_p)),
              ('y', ctypes.c_int)]
