import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1.0

def fun2():
    return 1.0

class Callable:
    def __call__(self):
        return 1.0

fun3 = Callable()

