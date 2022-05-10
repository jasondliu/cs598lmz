import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
free = _libraries['libgdk-3.so.0'].free
free.restype = None
free.argtypes = [ctypes.c_void_p]
malloc = _libraries['libgdk-3.so.0'].malloc
malloc.restype = ctypes.c_void_p
malloc.argtypes = [gsize]
memmove = _libraries['libgdk-3.so.0'].memmove
memmove.restype = ctypes.c_void_p
memmove.argtypes = [ctypes.c_void_p, ctypes.c_void_p, gsize]
memcpy = _libraries['libgdk-3.so.0'].memcpy
memcpy.restype = ctypes.c_void_p
memcpy.argtypes = [ctypes.c_void_p, ctypes.c_void_p, gsize]
memset = _libraries['libgdk-3.so.0'].memset
memset.restype = ctypes
