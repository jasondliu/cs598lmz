import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_long, ctypes.c_long, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.c_void_p)

c_module = ctypes.cdll.LoadLibrary('./c_module.so')


def c_module_wrap(X, Y, func):
    X_len, Y_len = len(X), len(Y)
    X_buf = (ctypes.c_double * (X_len + 1))()
    Y_buf = (ctypes.c_double * (Y_len + 1))()
    X_buf[:X_len] = X
    Y_buf[:Y_len] = Y
    return func(X_buf, Y_buf, ctypes.c_double(0.25), ctypes.c_double(0), ctypes.c_double(0))

c_module_func = c_module.trisum
c_module_func.argtypes = [ctypes.POINTER(ctypes.c_
