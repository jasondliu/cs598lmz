import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def callback(func):
    @wraps(func)
    def wrap(a,b,c):
        return func(a,b)
    return FUNTYPE(wrap)



def test_callback():
    @callback
    def fun(a,b):
        return a+b
    fun.argtypes=[ctypes.c_int,ctypes.c_int]
    fun.restype = ctypes.c_int
    fun(1,2)
    fun(1,2)
