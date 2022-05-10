import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_int,ctypes.c_void_p)

def callback(x,y):
    print("callback",x,y)
    #return x

#func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p)(callback)

#define callback function
#@void (*callback)(int, void *);
deliver_result_f = FUNTYPE(callback)

#register callback function
#@callback = deliver_result_f;

#sample_result_callback(callback, 0, buf);
ctypes.pythonapi.sample_result_callback.argtypes=(FUNTYPE,ctypes.c_int,ctypes.c_void_p)
ctypes.pythonapi.sample_result_callback(deliver_result_f,ctypes.c_int(0),ctypes.c_void_p())
