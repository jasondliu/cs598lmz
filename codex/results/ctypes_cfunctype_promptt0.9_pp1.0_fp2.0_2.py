import ctypes
# Test ctypes.CFUNCTYPE with an array argument

MIN = 0
MAX = 5

libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)

array = (ctypes.c_ushort * MAX)()

f = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.POINTER(ctypes.c_ushort)) # This works
#f = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.POINTER(ctypes.c_ushort), ctypes.c_uint, ctypes.c_uint) # As does this

# But this causes the error
#This function returned a result of type 'unsigned int' with an invalid index type 'POINTER(c_ushort)'.

#f = libc.pthread_create
#f.argtypes = (ctypes.c_void_p,
#            ctypes.c_void_p,
#            ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p),

