import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
f = fun()

# Y is not a CFUNCTYPE
class Y(int):
    def __init__(self, value):
        self.value = value
