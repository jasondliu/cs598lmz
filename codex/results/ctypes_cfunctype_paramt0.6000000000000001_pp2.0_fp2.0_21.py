import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def set_fun(fun):
    global _fun
    _fun = fun

def callback(data):
    print("callback called")
    _fun(data.encode('ascii'))
    return 0

CALLBACK = FUNTYPE(callback)

lib.set_callback(CALLBACK)

print("callback set")

lib.call_callback("hello")
</code>

