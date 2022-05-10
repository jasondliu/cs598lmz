import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)

class C_Callback(object):
    def __init__(self, callback):
        self.callback = callback
        self.c_callback = FUNTYPE(self.callback)

    def __call__(self, *args):
        return self.callback(*args)

def callback(f):
    return C_Callback(f)
</code>

