import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int, ctypes.c_int, ctypes.c_int)
glXGetProcAddress = None
glXGetProcAddress = _libGLX.glXGetProcAddress
glXGetProcAddress.restype = FUNTYPE
glXGetProcAddress.argtypes = [ctypes.c_char_p]
glXGetProcAddressARB = None
glXGetProcAddressARB = _libGLX.glXGetProcAddressARB
glXGetProcAddressARB.restype = FUNTYPE
glXGetProcAddressARB.argtypes = [ctypes.c_char_p]
XVisualInfo = _libGLX._XVisualInfo
XVisualInfo = _libGLX.XVisualInfo
XVisualInfo._fields_ = [
    ('ext_data', ctypes.c_char_p),
    ('visual', XVisual),
    ('visualid', VisualID),
    ('screen', ctypes.c_int),
    ('depth', ctypes.c_int),
    ('class', c
