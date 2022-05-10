import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)

def call_back(x,y,z):
    print 'callback: ', x, y, z

callback = FUNTYPE(call_back)

dll = ctypes.CDLL('test.dll')
dll.set_callback(callback)
dll.call_callback()
</code>

