import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_uint32), ctypes.c_uint32, ctypes.c_ubyte, ctypes.c_ubyte)
glBindBuffer = gl.glBindBuffer
glBindBuffer.argtypes = [ctypes.c_uint32, ctypes.c_uint32]
glBindBuffer.restype = None
glBufferData = gl.glBufferData
glBufferData.argtypes = [ctypes.c_uint32, ctypes.POINTER(ctypes.c_int), ctypes.c_void_p, ctypes.c_uint32]
glBufferData.restype = None
glBufferSubData = gl.glBufferSubData
glBufferSubData.argtypes = [ctypes.c_uint32, ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_void_p]
glBufferSubData.restype = None
glDeleteBuffers = gl.glDeleteBuffers
glDeleteBuffers.argtypes = [ctypes.c_int, ctypes.POINTER(ct
