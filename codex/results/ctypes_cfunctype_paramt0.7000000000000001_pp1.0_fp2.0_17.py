import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.c_int,
                           ctypes.c_int,
                           ctypes.c_int,
                           ctypes.c_int,
                           ctypes.c_int,
                           ctypes.c_int)

lib = ctypes.CDLL("C:\\Users\\Vlad\\Desktop\\pde\\pde\\Debug\\pde.dll")
# lib = ctypes.CDLL("C:\\Users\\vlad\\Desktop\\pde\\pde\\x64\\Release\\pde.dll")
# lib = ctypes.CDLL("C:\\Users\\vlad\\Desktop\\pde\\pde\\Debug\\pde.dll")
# lib = ctypes
