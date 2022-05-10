import ctypes
ctypes.cast(u_ptr, ctypes.c_void_p).value

u_ptr2 = scipy.ctypeslib.load_library("libmyscapi", ".")['_ZN4pyublas4test8main_cublasEiPPc']
u_ptr2

ctypes.cast(u_ptr2, ctypes.c_void_p).value

libcusolver_fnptr = scipy.ctypeslib.load_library("libcusolver_test", ".")['math_kernel']
libcusolver_fnptr

ctypes.cast(libcusolver_fnptr, ctypes.c_void_p).value

ctypes.cast(u_ptr, ctypes.c_void_p).value

ctypes.cast(u_ptr2, ctypes.c_void_p).value

libcusolver_fnptr2 = scipy.ctypeslib.load_library("libcusolver_test", ".")['math_kernel']

ctypes.cast(libcusolver_fnptr2, ctypes.c_void_p).
