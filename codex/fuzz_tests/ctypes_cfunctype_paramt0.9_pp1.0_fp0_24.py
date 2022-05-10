import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_uint8), 
                           ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint8))

zlib_orig = Zlib_DLL.inflate

zlib_callback = FUNTYPE(
    lambda data, size, buffer:
        print("callback data: '%s'" % data) or 0
)

# in order to simplify the test, pass wrapped pyfunc that doesn't callback
zlib_callbackex = FUNTYPE(
    lambda data, size, buffer:
        zlib_callback(data, size, buffer) or 0
)

zlib_callback_handle = Zlib_DLL.zlib_callback_handle
zlib_callback_handle.argtypes = [ctypes.c_void_p, FUNTYPE, FUNTYPE]
zlib_callback_handle.restype = ctypes.c_void_p

def inflate(data):
    global Zlib_DLL
    out = ctypes.create_string_buffer(
