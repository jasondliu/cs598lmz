import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'fun called'

def main():
    fun_ptr = FUNTYPE(fun)
    print(fun_ptr())
    print(sys.getrefcount(fun_ptr))
    print(sys.getrefcount(fun))

