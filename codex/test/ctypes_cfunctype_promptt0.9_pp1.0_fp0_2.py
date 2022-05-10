import ctypes
# Test ctypes.CFUNCTYPE
class GLFWVidMode(ctypes.Structure):
    _fields_ = [("width", ctypes.c_int),
                ("height", ctypes.c_int),
                ("redBits", ctypes.c_int),
                ("greenBits", ctypes.c_int),
                ("blueBits", ctypes.c_int),
                ("refreshRate", ctypes.c_int)]
