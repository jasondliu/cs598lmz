import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def myfunc(a, b):
    print('Hello from a callback!')
    return a * b
mycallback = FUNTYPE(myfunc)
mycallback(2, 3)

# ctypes.POINTER(ctypes.c_int)

# ctypes.c_int.in_dll(libc, 'errno')

# ctypes.CDLL(None).errno

# ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.py_object(exctype))

# ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), 0)

# ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.py_object(exctype))

# ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.c_long(0))
