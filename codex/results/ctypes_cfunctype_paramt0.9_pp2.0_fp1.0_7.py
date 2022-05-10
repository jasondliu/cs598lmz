import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
class Test(ctypes.Structure):
    _fields_ = [("callback",FUNTYPE)]
    def __init__(self,callback):
        self.callback = callback

@FUNTYPE
def print_hello():
    print("Hello")

a=Test(print_hello)
a.callback()
</code>

