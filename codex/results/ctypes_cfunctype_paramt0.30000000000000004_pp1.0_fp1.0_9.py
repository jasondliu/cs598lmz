import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class PyEvent(ctypes.Structure):
    _fields_ = [("type", ctypes.c_int),
                ("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("button", ctypes.c_int),
                ("mod", ctypes.c_int),
                ("key", ctypes.c_int),
                ("unicode", ctypes.c_int),
                ("scancode", ctypes.c_int),
                ("window", ctypes.c_void_p),
                ("userdata", ctypes.c_void_p)]

class PyEventType(object):
    QUIT = 0
    KEYDOWN = 1
    KEYUP = 2
    MOUSEMOTION = 3
    MOUSEBUTTONDOWN = 4
    MOUSEBUTTONUP = 5
    VIDEORESIZE = 6
    VIDEOEXPOSE = 7
    USEREVENT = 8

class PyEventMod(object):
    NONE = 0
    LSHIFT = 1
    RSHIFT = 2
