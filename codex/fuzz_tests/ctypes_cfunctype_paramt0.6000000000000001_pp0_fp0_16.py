import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
FUNTYPE2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_void_p)


def f_callback(n, array):
    for i in range(n):
        array[i] = array[i] * 2
    return 0

def f_callback2(n, array, userdata):
    for i in range(n):
        array[i] = array[i] * 2
    return 0

callback = FUNTYPE(f_callback)
callback2 = FUNTYPE2(f_callback2)

dll.f(5, callback)
dll.f2(5, callback2, None)
</code>

