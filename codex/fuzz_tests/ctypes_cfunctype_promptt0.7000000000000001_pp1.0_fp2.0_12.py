import ctypes
# Test ctypes.CFUNCTYPE
class rdwr_func(ctypes.Structure):
    _fields_ = [('read', ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p)),
                ('write', ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p))]
 
# Test ctypes.c_ubyte and ctypes.POINTER(ctypes.c_ubyte)
class rdwr_buf(ctypes.Structure):
    _fields_ = [('base', ctypes.POINTER(ctypes.c_ubyte)),
                ('len', ctypes.c_size_t)]
 
# Test ctypes.c_void_p and ctypes.c_size_
