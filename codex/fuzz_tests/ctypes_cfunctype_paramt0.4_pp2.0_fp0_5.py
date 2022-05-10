import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def callback(msg):
    print('Callback:', msg)
    return 0

CALLBACK = FUNTYPE(callback)

dll = ctypes.CDLL('libpycall.dll')
dll.pycall(CALLBACK)
</code>

