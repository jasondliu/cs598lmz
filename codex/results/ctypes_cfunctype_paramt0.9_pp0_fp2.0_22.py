import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
# Note: return value ignored
def kpxmls_callback_wrapper(callback, context, name, value, metadata):
    return callback(context, name, value, metadata)
kpxmls_callback = FUNTYPE(kpxmls_callback_wrapper)

# Note: xml-pointer returned needs to be (at some point) free()'d

lib.kpxmls_load.argtypes = [ctypes.c_char_p, kpxmls_callback, ctypes.c_void_p]
lib.kpxmls_load.restype = ctypes.c_void_p
lib.kpxmls_by_class.argtypes = [ctypes.c_void_p, ctypes.c_char_p, kpxmls_callback, ctypes.c_void_p]
lib.kpxmls_by_
